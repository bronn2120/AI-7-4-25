import sqlite3
import os
from dotenv import load_dotenv  # Fits your existing env usage in chat_agent.py

load_dotenv()

DB_PATH = os.path.join(os.path.dirname(__file__), 'company.db')  # In core/

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

def list_all_entries():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM dealer_info")
    results = c.fetchall()
    conn.close()
    if not results:
        return "No entries in database."
    # Print in table format (fits for console check in autonomous company monitoring)
    print("ID | Brand | Component | Info (truncated to 100 chars)")
    print("-" * 50)
    for row in results:
        id, brand, info, component = row
        truncated_info = info[:100] + '...' if len(info) > 100 else info
        print(f"{id} | {brand} | {component} | {truncated_info}")
    return results  # Return full for integration in agents

# Test block (run standalone: python core/db.py)
if __name__ == "__main__":
    init_sqlite()  # Creates table if not exists
    insert_dealer_info("Lutron", "Test info: Reset bridge for no sound.", "audio")  # Example insert
    print(query_sqlite("Lutron", "audio"))  # Should print the inserted info
    list_all_entries()  # Prints all