import os
import subprocess
import json
from dotenv import load_dotenv  # Fits your existing env loading in chat_agent.py
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Root path for core/ 
from langgraph.graph import StateGraph, END  # Fits LangGraph 0.2.20 deps
from typing import Dict, List, TypedDict
from langchain_core.messages import HumanMessage
from langchain_openai import OpenAIEmbeddings  # Embeddings fit (dynamic for variable data)
from pinecone import Pinecone as PineconeClient  # Fits your pc/init in chat_agent.py
from core.db import insert_dealer_info, query_sqlite  # Hybrid fit from db.py

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")  # Fits your embeddings; dynamic/variable length (Grok 4 placeholder: model="grok-4" when API ready)
pc = PineconeClient(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("troubleshooter-index")  # Fits your index

class State(TypedDict):
    messages: List[str]
    scraped_data: List[Dict[str, str]]

def scrape_agent(state: State) -> State:
    scraped_data = []  # Collect yielded items from JSON
    # Run Scrapy via subprocess (fits your nested path; avoids import issues, preserves spider 100%)
    spider_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scrapy-selenium', 'lutron_scraper', 'lutron_scraper'))  # Change dir to your project root for run
    output_file = '/tmp/scraped_items.json'  # Temp JSON in /tmp to avoid dir issues
    try:
        subprocess.call(['scrapy', 'crawl', 'lutron', '-o', output_file], cwd=spider_dir)  # Run spider, output to JSON (name 'lutron' fits your bot)
        with open(output_file, 'r') as f:
            scraped_data = json.load(f)  # Load yielded items (fits your spider yield dicts)
        os.remove(output_file)  # Clean up
        print("Debug: Scraped data keys and sample: ", scraped_data[0] if scraped_data else "No items scraped")  # Debug for keys
    except Exception as e:
        print(f"Scrapy run error: {e}")  # Log; continue with empty for test
    # Process collected items (fits your vector loading note—dynamic on 'solution')
    for item in scraped_data:
        info = item.get('solution', ' '.join(str(v) for v in item.values()))  # Use 'solution' or concat all
        component = item.get('product', 'unknown')  # From your debug keys
        insert_dealer_info("Lutron", info, component)  # Hybrid to SQLite (full text, no limit)
        # Dynamic upsert to Pinecone (batch for efficiency, variable lengths)
        emb = embeddings.embed_query(info)  # Embed full for search
        metadata_solution = info[:40000]  # Truncate to <40KB for metadata limit (fits Pinecone best practice)
        index.upsert([{"id": str(hash(info)), "values": emb, "metadata": {"solution": metadata_solution, "brand": "Lutron", "issue": item.get('issue', ''), "category": item.get('category', ''), "url": item.get('url', '')}}])
    return {"scraped_data": scraped_data, "messages": state["messages"] + ["Scraped Lutron data"]}

def query_agent(state: State) -> State:
    # Hybrid query (fits retrieval in chat_agent.py)
    emb = embeddings.embed_query("Lutron rack issue")
    results = index.query(vector=emb, top_k=1, include_metadata=True).get('matches', [])
    pinecone_result = results[0].get('metadata', {}).get('solution', '') if results else 'No Pinecone matches'
    sqlite_result = query_sqlite("Lutron", "audio")  # Example; dynamic from input/issue later
    combined = f"Pinecone: {pinecone_result}\nSQLite: {sqlite_result}"
    return {"messages": state["messages"] + [combined]}

graph = StateGraph(State)
graph.add_node("scrape", scrape_agent)
graph.add_node("query", query_agent)
graph.add_edge("scrape", "query")
graph.add_edge("query", END)
graph.set_entry_point("scrape")
app = graph.compile()

# Test block (run standalone: python graphs/lutron_basic_graph.py; runs crawl, prints state with scraped + hybrid)
if __name__ == "__main__":
    initial_state = {"messages": [], "scraped_data": []}
    result = app.invoke(initial_state)
    print(result)  # Output: {'messages': ['Scraped Lutron data', 'Pinecone: ... \nSQLite: ...'], 'scraped_data': [{'issue': ..., 'solution': ..., 'product': ..., ...}, ...]}