# Import necessary libraries
from pydantic import BaseModel
from typing import Dict, Optional
import os
from dotenv import load_dotenv
import time
import random
import requests
from bs4 import BeautifulSoup
from langgraph.graph import Graph
import getpass
from openai import OpenAI

# Load environment variables from .env file
load_dotenv(dotenv_path='/home/vincent/x/langgraph/examples/rag/.env', override=True)

# Verify and set XAI_API_KEY
xai_api_key = os.getenv("XAI_API_KEY")
if xai_api_key:
    print(f"Loaded XAI API key: {xai_api_key[:5]}... (hidden for security)")
else:
    print("XAI_API_KEY not found in .env file!")
    os.environ["XAI_API_KEY"] = getpass.getpass("Please enter XAI_API_KEY: ")

# Initialize OpenAI client for xAI's Grok API
client = OpenAI(
    api_key=xai_api_key,
    base_url="https://api.x.ai/v1"  # Updated to xAI's standard endpoint
)

# Define Pydantic models
class PerformanceData(BaseModel):
    ranking: int
    traffic: int
    timestamp: str

class Task(BaseModel):
    agent: str
    action: str
    priority: int
    details: Dict

class AgentState(BaseModel):
    task: Optional[Task] = None
    performance_data: Optional[PerformanceData] = None
    result: Dict = {}

# Helper functions
def get_top_5_urls(keyword: str) -> list:
    """Simulate fetching top 5 URLs for a keyword."""
    print(f"Simulating search for '{keyword}'")
    return [f"https://example.com/{i}" for i in range(1, 6)]

def scrape_website(url: str) -> str:
    """Scrape content from a URL with error handling."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text(separator=' ', strip=True)[:2000]
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "Scraping failed"

# SEO Agent task handlers
def optimize_content(details: Dict) -> Dict:
    """Optimize content for SEO using the Grok API."""
    keyword = details.get("keyword", "default_keyword")
    content = details.get("content", "Sample content for AI chat agent support")
    prompt = f"Optimize this content for SEO around '{keyword}':\n{content}"
    try:
        response = client.chat.completions.create(
            model="grok-3",  # Updated model name
            messages=[{"role": "user", "content": prompt}]
        )
        print(f"SEO Agent - Optimize Content - Response: {response}")
        if not hasattr(response, 'choices') or not response.choices:
            print("SEO Agent - Debug: No valid 'choices' in response")
            return {"status": "error", "message": "No valid 'choices' in API response"}
        choice = response.choices[0]
        if not hasattr(choice, 'message') or not choice.message:
            print("SEO Agent - Debug: No valid 'message' in choice")
            return {"status": "error", "message": "No valid 'message' in API response"}
        optimized_content = choice.message.content
        if optimized_content is None:
            print("SEO Agent - Debug: Content is None")
            return {"status": "error", "message": "Content is None in API response"}
        return {"status": "success", "optimized_content": optimized_content, "message": "Content optimized successfully"}
    except Exception as e:
        print(f"SEO Agent - Optimize Content - Error: {type(e).__name__}: {str(e)}")
        return {"status": "error", "message": f"Failed to optimize content: {str(e)}"}

def research_keywords(details: Dict) -> Dict:
    """Generate SEO-friendly keywords using the Grok API."""
    topic = details.get("topic", "default_topic")
    prompt = f"Generate a list of 10 SEO-friendly keywords for the topic '{topic}'."
    try:
        response = client.chat.completions.create(
            model="grok-3",
            messages=[{"role": "user", "content": prompt}]
        )
        print(f"SEO Agent - Research Keywords - Response: {response}")
        if not hasattr(response, 'choices') or not response.choices:
            print("SEO Agent - Debug: No valid 'choices' in response")
            return {"status": "error", "message": "No valid 'choices' in API response"}
        choice = response.choices[0]
        if not hasattr(choice, 'message') or not choice.message:
            print("SEO Agent - Debug: No valid 'message' in choice")
            return {"status": "error", "message": "No valid 'message' in API response"}
        keywords = choice.message.content
        if keywords is None:
            print("SEO Agent - Debug: Content is None")
            return {"status": "error", "message": "Content is None in API response"}
        return {"status": "success", "keywords": keywords, "message": "Keywords generated successfully"}
    except Exception as e:
        print(f"SEO Agent - Research Keywords - Error: {type(e).__name__}: {str(e)}")
        return {"status": "error", "message": f"Failed to research keywords: {str(e)}"}

def analyze_competitors(details: Dict) -> Dict:
    """Analyze competitors' content using the Grok API."""
    keyword = details.get("keyword", "default_keyword")
    top_urls = get_top_5_urls(keyword)
    analysis = ""
    for url in top_urls:
        content = scrape_website(url)
        prompt = f"Analyze this content and explain why it might rank high for '{keyword}':\n{content}"
        try:
            response = client.chat.completions.create(
                model="grok-3",
                messages=[{"role": "user", "content": prompt}]
            )
            print(f"SEO Agent - Analyze Competitors ({url}) - Response: {response}")
            if not hasattr(response, 'choices') or not response.choices:
                analysis += f"\n{url}: No valid 'choices' in response"
            else:
                choice = response.choices[0]
                if not hasattr(choice, 'message') or not choice.message:
                    analysis += f"\n{url}: No valid 'message' in choice"
                else:
                    analysis += f"\n{url}: {choice.message.content or 'No content'}"
        except Exception as e:
            print(f"SEO Agent - Analyze Competitors ({url}) - Error: {type(e).__name__}: {str(e)}")
            analysis += f"\n{url}: Failed - {str(e)}"
    return {"status": "success", "analysis": analysis, "message": "Competitor analysis completed"}

# SEO Agent node
def se_node(state: AgentState) -> AgentState:
    """SEO Agent node to handle tasks."""
    task = state.task
    print(f"SEO Agent: Performing {task.action} with details {task.details}")
    if task.action == "optimize_content":
        result = optimize_content(task.details)
    elif task.action == "research_keywords":
        result = research_keywords(task.details)
    elif task.action == "analyze_competitors":
        result = analyze_competitors(task.details)
    else:
        result = {"status": "error", "message": "Unknown action"}
    state.result = result
    print(f"SEO Agent: {result['message']}")
    return state

# CEO Agent node
def ceo_node(state: AgentState) -> AgentState:
    """CEO Agent node to assign tasks."""
    data = state.performance_data
    print(f"CEO Agent: Analyzing performance - Ranking: {data.ranking}, Traffic: {data.traffic}")
    # Force an SEO task for testing
    task = Task(
        agent="SE",
        action="optimize_content",
        priority=1,
        details={"keyword": "AI chat agent", "content": "Support for AI-driven chat solutions", "urgency": "high"}
    )
    state.task = task
    print(f"CEO Agent: Assigned task to {task.agent} - Action: {task.action}, Priority: {task.priority}")
    return state

# Placeholder nodes
def content_node(state: AgentState) -> AgentState:
    """Placeholder Content Agent."""
    print(f"Content Agent: Performing {state.task.action} with details {state.task.details}")
    time.sleep(2)
    state.result = {"status": "success", "message": f"Content created on {state.task.details['topic']}"}
    return state

def maintenance_node(state: AgentState) -> AgentState:
    """Placeholder Maintenance Agent."""
    print(f"Maintenance Agent: Performing {state.task.action} with details {state.task.details}")
    time.sleep(2)
    state.result = {"status": "success", "message": "Maintenance task completed"}
    return state

# Simulate performance data
def fetch_performance_data():
    """Simulate performance data."""
    ranking = random.randint(1, 10)
    traffic = random.randint(300, 2000)  # Adjusted to allow Content tasks
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    return PerformanceData(ranking=ranking, traffic=traffic, timestamp=timestamp)

# Set up LangGraph workflow
graph = Graph()
graph.add_node("ceo", ceo_node)
graph.add_node("se", se_node)
graph.add_node("content", content_node)
graph.add_node("maintenance", maintenance_node)

graph.add_conditional_edges(
    "ceo",
    lambda state: state.task.agent,
    {"SE": "se", "Content": "content", "Maintenance": "maintenance"}
)

graph.set_finish_point("se")
graph.set_finish_point("content")
graph.set_finish_point("maintenance")
graph.set_entry_point("ceo")

# Compile and run
app = graph.compile()

if __name__ == "__main__":
    print("Starting CEO and SEO Agents...")
    for _ in range(3):
        performance_data = fetch_performance_data()
        print(f"\n=== Iteration ===\nPerformance Data - Ranking: {performance_data.ranking}, Traffic: {performance_data.traffic}")
        state = AgentState(performance_data=performance_data)
        result = app.invoke(state)
        print("Task Result:", result.result)
        time.sleep(2)