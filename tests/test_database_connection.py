import os
import sqlite3
DB_PATH = os.path.join("data", "crypto_prices.db")
def test_database_connection():
    assert os.path.exists(DB_PATH), "Database file does not exist!"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='prices';")
    table = cursor.fetchone()
    conn.close()
    assert table is not None, "Prices table does not exist!"