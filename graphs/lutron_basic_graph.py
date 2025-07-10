import os
from dotenv import load_dotenv  # Fits your existing env loading
from langgraph.graph import StateGraph, END  # Updated API for LangGraph 0.2.20 (fits your graph in chat_agent.py)
from typing import Dict, List, TypedDict
from langchain_core.messages import HumanMessage
from langchain_openai import OpenAIEmbeddings  # Embeddings from your chat_agent.py fit
from pinecone import Pinecone as PineconeClient  # Fits your pc
from scrapy.crawler import CrawlerProcess
# Assume your spider path; adjust if different (e.g., from scrapy_selenium.lutron_scraper.spiders import LutronSpider)
from scrapy_selenium.lutron_scraper.spiders.your_lutron_spider import LutronSpider  # Preserve your spider; replace 'your_lutron_spider' with actual file/class name
from core.db import insert_dealer_info, query_sqlite  # Hybrid DB fit

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")  # Fits your embeddings; dynamic for variable data
pc = PineconeClient(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("troubleshooter-index")  # Fits your index name

class State(TypedDict):
    messages: List[str]
    scraped_data: List[Dict[str, str]]

def scrape_agent(state: State) -> State:
    process = CrawlerProcess()
    process.crawl(LutronSpider)  # Your existing spider; preserves parse/output
    process.start()
    scraped = []  # Extract from spider (fit your code: e.g., scraped = process.crawlers.list()[0].spider.items or yield loop)
    # Example: Assume spider yields {'info': 'Lutron reset', 'component': 'audio'}
    for item in scraped:  # Replace with actual extraction
        insert_dealer_info("Lutron", item.get('info', ''), item.get('component', ''))  # Hybrid store to SQLite
        # Dynamic upsert to Pinecone (fits your note on variable lengths; batch for efficiency)
        emb = embeddings.embed_query(item.get('info', 'unknown'))
        index.upsert([{"id": str(hash(item['info'])), "values": emb, "metadata": {"solution": item['info'], "brand": "Lutron"}}])
    return {"scraped_data": scraped, "messages": state["messages"] + ["Scraped Lutron data"]}

def query_agent(state: State) -> State:
    # Hybrid query (fits retrieval in chat_agent.py)
    emb = embeddings.embed_query("Lutron rack issue")
    pinecone_result = index.query(vector=emb, top_k=1, include_metadata=True).get('matches', [{}])[0].get('metadata', {}).get('solution', '')
    sqlite_result = query_sqlite("Lutron", "audio")  # Example component; dynamic based on input later
    combined = f"Pinecone: {pinecone_result}\nSQLite: {sqlite_result}"
    return {"messages": state["messages"] + [combined]}

graph = StateGraph(State)
graph.add_node("scrape", scrape_agent)
graph.add_node("query", query_agent)
graph.add_edge("scrape", "query")
graph.add_edge("query", END)
graph.set_entry_point("scrape")
app = graph.compile()

# Test block (run standalone: python graphs/lutron_basic_graph.py; prints result with scraped + hybrid query)
if __name__ == "__main__":
    initial_state = {"messages": [], "scraped_data": []}
    result = app.invoke(initial_state)
    print(result)  # Example output: {'messages': ['Scraped Lutron data', 'Pinecone: ... \nSQLite: ...'], 'scraped_data': [...]}