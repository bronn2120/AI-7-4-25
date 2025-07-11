import os
import sys
from dotenv import load_dotenv  # Fits your existing env loading in chat_agent.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scrapy-selenium')))  # Added: Includes your local scrapy-selenium dir to fix ModuleNotFoundError
from langgraph.graph import StateGraph, END  # Fits LangGraph 0.2.20 deps
from typing import Dict, List, TypedDict
from langchain_core.messages import HumanMessage
from langchain_openai import OpenAIEmbeddings  # Embeddings fit (dynamic for variable data)
from pinecone import Pinecone as PineconeClient  # Fits your pc/init in chat_agent.py
from scrapy.crawler import CrawlerRunner  # Updated: Runner for async script run with reactor (fits Scrapy)
from scrapy.utils.log import configure_logging
from twisted.internet import reactor, defer  # For collecting yielded items in script
# Assume your spider; adjust if class/file different (e.g., from lutron_scraper.spiders.spiders import LutronSpider if file is spiders.py)
from lutron_scraper.spiders.lutron_spider import LutronSpider  # Preserve your spider; replace 'lutron_spider' with actual file name (no .py)
from core.db import insert_dealer_info, query_sqlite  # Hybrid fit from db.py

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")  # Fits your embeddings; dynamic/variable length
pc = PineconeClient(api_key=os.getenv("PINECONE_API_KEY"))
index = pc.Index("troubleshooter-index")  # Fits your index

class State(TypedDict):
    messages: List[str]
    scraped_data: List[Dict[str, str]]

def scrape_agent(state: State) -> State:
    scraped_data = []  # Collect yielded items
    def item_scraped(item, response, spider):
        scraped_data.append(item)  # Append yielded item from spider
        return item

    configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})  # Optional logging
    runner = CrawlerRunner()
    d = runner.crawl(LutronSpider)  # Your existing spider; preserves parse/start_urls
    d.addBoth(lambda _: reactor.stop())  # Stop reactor after crawl
    # Connect signal for item_scraped (fits Scrapy to collect in script)
    from scrapy.signals import item_scraped as signal_item_scraped
    runner.crawlers.pop().signals.connect(item_scraped, signal=signal_item_scraped)
    reactor.run()  # Run the crawl
    # Process collected items (fits your vector loading note)
    for item in scraped_data:
        insert_dealer_info("Lutron", item.get('info', ''), item.get('component', ''))  # Hybrid to SQLite
        # Dynamic upsert to Pinecone (batch for efficiency, variable lengths)
        emb = embeddings.embed_query(item.get('info', 'unknown'))
        index.upsert([{"id": str(hash(item['info'])), "values": emb, "metadata": {"solution": item['info'], "brand": "Lutron"}}])
    return {"scraped_data": scraped_data, "messages": state["messages"] + ["Scraped Lutron data"]}

def query_agent(state: State) -> State:
    # Hybrid query (fits retrieval in chat_agent.py)
    emb = embeddings.embed_query("Lutron rack issue")
    pinecone_result = index.query(vector=emb, top_k=1, include_metadata=True).get('matches', [{}])[0].get('metadata', {}).get('solution', '')
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
    print(result)  # Output: {'messages': ['Scraped Lutron data', 'Pinecone: ... \nSQLite: ...'], 'scraped_data': [{'info': ..., 'component': ...}, ...]}