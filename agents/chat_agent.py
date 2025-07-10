import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import json
import logging
import asyncio
from google.cloud import speech, vision
from langgraph.graph import Graph
from typing import Dict, Any, Optional
from pydantic import BaseModel
from openai import OpenAI
from pinecone import Pinecone as PineconeClient
import cv2
import numpy as np
from dotenv import load_dotenv
import getpass
import time
from langchain_openai import OpenAIEmbeddings  # Added: For dynamic ADA-003 embeddings (fits your OpenAI usage; handles variable lengths)
from core.db import insert_dealer_info, query_sqlite  # Added: SQLite hybrid for exact matches (fits your note on 100% answers with Pinecone)

# Load environment variables (unchanged)
load_dotenv(dotenv_path='/home/vincent/ixome/.env', override=True)

# Initialize logging (unchanged)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Verify and set API keys (unchanged)
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    logger.error("OPENAI_API_KEY not found in .env file!")
    openai_api_key = getpass.getpass("Please enter OPENAI_API_KEY: ")
    os.environ["OPENAI_API_KEY"] = openai_api_key

pinecone_api_key = os.getenv("PINECONE_API_KEY")
if not pinecone_api_key:
    logger.error("PINECONE_API_KEY not found in .env file!")
    pinecone_api_key = getpass.getpass("Please enter PINECONE_API_KEY: ")
    os.environ["PINECONE_API_KEY"] = pinecone_api_key

google_credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
if not google_credentials_path:
    logger.error("GOOGLE_APPLICATION_CREDENTIALS not found in .env file!")
    google_credentials_path = getpass.getpass("Please enter GOOGLE_APPLICATION_CREDENTIALS path: ")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_credentials_path

# Initialize clients (added embeddings for dynamic; fits Grok 4 fallback later)
client = OpenAI(api_key=openai_api_key)
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")  # ADA-003 style; dynamic, variable length (replace model with "grok-4" when xAI API ready)
pc = PineconeClient(api_key=pinecone_api_key)
speech_client = speech.SpeechClient()
vision_client = vision.ImageAnnotatorClient()

# Initialize Pinecone index (unchanged)
index_name = "troubleshooter-index"
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=3072,  # Dimension for text-embedding-3-large
        metric='cosine',
        spec={'serverless': {'cloud': 'aws', 'region': os.getenv("PINECONE_ENVIRONMENT", "us-east-1")}}
    )
index = pc.Index(index_name)

# Define Pydantic models (unchanged)
class ClientQuery(BaseModel):
    query: str
    client_id: Optional[str] = None
    timestamp: str

class Solution(BaseModel):
    solution: str
    confidence: float
    source: Optional[str] = None

class AgentState(BaseModel):
    input_type: Optional[str] = None
    input_data: Optional[Any] = None
    query: Optional[ClientQuery] = None
    processed_input: Optional[str] = None
    issue: Optional[str] = None
    solution: Optional[Solution] = None
    result: Dict = {}

class ChatAgent:
    def __init__(self):
        self.logger = logger
        self.client = client
        self.speech_client = speech_client
        self.vision_client = vision_client
        self.index = index

        # Set up LangGraph workflow (unchanged)
        self.graph = Graph()
        self.graph.add_node("input", self.input_node)
        self.graph.add_node("text_processing", self.text_processing_node)
        self.graph.add_node("voice_processing", self.voice_processing_node)
        self.graph.add_node("video_processing", self.video_processing_node)
        self.graph.add_node("issue_identification", self.issue_identification_node)
        self.graph.add_node("solution_retrieval", self.solution_retrieval_node)
        self.graph.add_node("response_generation", self.response_generation_node)

        self.graph.add_conditional_edges(
            "input",
            lambda state: state.input_type or "text",
            {"text": "text_processing", "voice": "voice_processing", "video": "video_processing"}
        )
        self.graph.add_edge("text_processing", "issue_identification")
        self.graph.add_edge("voice_processing", "issue_identification")
        self.graph.add_edge("video_processing", "issue_identification")
        self.graph.add_edge("issue_identification", "solution_retrieval")
        self.graph.add_edge("solution_retrieval", "response_generation")
        self.graph.set_entry_point("input")
        self.graph.set_finish_point("response_generation")
        self.app = self.graph.compile()

    async def input_node(self, state: AgentState) -> AgentState:
        self.logger.info(f"Received input: type={state.input_type}, data=<data>")
        return state

    async def text_processing_node(self, state: AgentState) -> AgentState:
        if state.query and state.query.query:
            state.processed_input = state.query.query
            self.logger.info(f"Processed text input: {state.processed_input}")
        else:
            state.processed_input = ""
            self.logger.warning("No query provided for text processing")
        return state

    async def voice_processing_node(self, state: AgentState) -> AgentState:
        audio_data = state.input_data or b""
        if audio_data:
            try:
                audio = speech.RecognitionAudio(content=audio_data)
                config = speech.RecognitionConfig(
                    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                    language_code='en-US'
                )
                response = self.speech_client.recognize(config=config, audio=audio)
                if response.results:
                    state.processed_input = response.results[0].alternatives[0].transcript
                    self.logger.info(f"Processed voice input: {state.processed_input}")
                else:
                    state.processed_input = "No speech detected"
                    self.logger.info("No speech detected in audio")
            except Exception as e:
                self.logger.error(f"Error processing voice: {e}")
                state.processed_input = "Error processing voice"
        else:
            state.processed_input = "No audio data provided"
            self.logger.warning("No audio data provided for voice processing")
        return state

    async def video_processing_node(self, state: AgentState) -> AgentState:
        video_data = state.input_data or b""
        if video_data:
            try:
                temp_file = "temp_video.mp4"
                with open(temp_file, "wb") as f:
                    f.write(video_data)
                cap = cv2.VideoCapture(temp_file)
                frame_descriptions = []
                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break
                    _, buffer = cv2.imencode('.jpg', frame)
                    image = vision.Image(content=buffer.tobytes())
                    response = self.vision_client.label_detection(image=image)
                    labels = [label.description for label in response.label_annotations]
                    frame_descriptions.append(", ".join(labels))
                cap.release()
                os.remove(temp_file)
                state.processed_input = "; ".join(frame_descriptions[:3]) if frame_descriptions else "No labels detected"
                self.logger.info(f"Processed video input: {state.processed_input}")
            except Exception as e:
                self.logger.error(f"Error processing video: {e}")
                state.processed_input = "Error processing video"
        else:
            state.processed_input = "No video data provided"
            self.logger.warning("No video data provided for video processing")
        return state

    async def issue_identification_node(self, state: AgentState) -> AgentState:
        processed_input = state.processed_input.lower() if state.processed_input else ""
        self.logger.info(f"Identifying issue from: {processed_input}")
        if any(phrase in processed_input for phrase in ["no sound", "sound not working", "surround sound", "audio issue"]):
            state.issue = "no_sound"
        elif "tv not turning on" in processed_input:
            state.issue = "tv_not_turning_on"
        elif "settings" in processed_input:
            state.issue = "settings_issue"
        elif any(phrase in processed_input for phrase in ["flashing light", "error code", "blinking"]):
            state.issue = "error_code"
        else:
            state.issue = "unknown"
        self.logger.info(f"Identified issue: {state.issue}")
        return state

    async def solution_retrieval_node(self, state: AgentState) -> AgentState:
        try:
            # Dynamic embedding with ADA-003 via LangChain (fits your note on variable lengths; replaces fixed client.create for flexibility)
            embedding_input = state.processed_input or "unknown issue"
            embedding = embeddings.embed_query(embedding_input)  # LangChain handles dynamic inputs/variables
            results = self.index.query(vector=embedding, top_k=1, include_metadata=True)
            if results['matches']:
                solution_text = results['matches'][0]['metadata'].get('solution', "No solution found")
                confidence = results['matches'][0]['score']
                # Hybrid: Append SQLite exact match (for 100% answers, pairs with vectors as per your note)
                brand = "Lutron" if "lutron" in embedding_input.lower() else "Unknown"  # Example detection; expand for Control4 etc.
                component = state.issue if state.issue else "Unknown"
                sqlite_result = query_sqlite(brand, component)
                solution_text += f"\nExact dealer info from SQLite: {sqlite_result}"
                state.solution = Solution(solution=solution_text, confidence=confidence, source="Pinecone + SQLite Hybrid")
                self.logger.info(f"Retrieved hybrid solution: {solution_text}")
                return state
        except Exception as e:
            self.logger.error(f"Pinecone/SQLite query failed: {e}")

        # Fallback solutions (unchanged, but add example insert for SQLite test—remove after initial run)
        solutions = {
            "no_sound": "Check if the sound system is turned on and cables are connected.",
            "tv_not_turning_on": "Ensure the TV is plugged in and the power cable is secure.",
            "settings_issue": "Navigate to the settings menu and verify the correct input source.",
            "error_code": "Note the flashing light pattern and consult the device manual."
        }
        solution_text = solutions.get(state.issue, "Issue not recognized. Please provide more details.")
        # Example insert to SQLite for test (fits Lutron focus; run once)
        insert_dealer_info("Lutron", "Dealer tip: Reset Lutron bridge for audio issues.", "audio")
        state.solution = Solution(solution=solution_text, confidence=0.5, source="Fallback")
        self.logger.info(f"Retrieved fallback solution: {solution_text}")
        return state

    async def response_generation_node(self, state: AgentState) -> AgentState:
        if state.solution and state.solution.solution:
            response = f"Little Einstein: {state.solution.solution}"
        else:
            response = "Little Einstein: No specific solution found. Please check the device manual or contact support."
        state.result = {"status": "success", "response": response, "message": "Solution provided"}
        self.logger.info(f"Generated response: {response}")
        return state

    async def process_input(self, input_type: str, input_data: Any) -> Dict[str, Any]:
        state = AgentState(
            input_type=input_type,
            input_data=input_data if input_type != "text" else None,
            query=ClientQuery(query=input_data if input_type == "text" else "", timestamp=time.strftime("%Y-%m-%d %H:%M:%S"))
        )
        result = await self.app.ainvoke(state)
        return result.result

if __name__ == "__main__":
    async def test():
        agent = ChatAgent()
        response = await agent.process_input("text", "My TV has no sound.")
        print(f"Text Response: {response}")
        try:
            with open("/home/vincent/ixome/notebooks/test_audio.wav", "rb") as f:
                response = await agent.process_input("voice", f.read())
            print(f"Voice Response: {response}")
        except FileNotFoundError:
            print("Voice test skipped: test_audio.wav not found")
        try:
            with open("/home/vincent/ixome/notebooks/test_video.mp4", "rb") as f:
                response = await agent.process_input("video", f.read())
            print(f"Video Response: {response}")
        except FileNotFoundError:
            print("Video test skipped: test_video.mp4 not found")
    asyncio.run(test())