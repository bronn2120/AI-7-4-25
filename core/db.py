import sqlite3
import os
from dotenv import load_dotenv  # Fits your existing env usage in chat_agent.py

load_dotenv()  # Load .env if needed (e.g., for future expansions; safe)

DB_PATH = os.path.join(os.path.dirname(__file__), 'company.db')  # In core/ dir

def init_sqlite():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS dealer_info
                 (id INTEGER PRIMARY KEY, brand TEXT, info TEXT, component TEXT)''')
    conn.commit()
    conn.close()

def insert_dealer_info(brand, info, component):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO dealer_info (brand, info, component) VALUES (?, ?, ?)", (brand, info, component))
    conn.commit()
    conn.close()

def query_sqlite(brand, component):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT info FROM dealer_info WHERE brand=? AND component=?", (brand, component))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "No exact dealer info found—check Pinecone for similar."

# Test block (run standalone: python core/db.py)
if __name__ == "__main__":
    init_sqlite()  # Creates table if not exists
    insert_dealer_info("Lutron", "Test info: Reset bridge for no sound.", "audio")  # Example insert
    print(query_sqlite("Lutron", "audio"))  # Should print the inserted info