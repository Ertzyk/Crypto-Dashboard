import requests
import pandas as pd
import sqlite3
from datetime import datetime, timezone
import os

COINS = ["bitcoin", "ethereum"]
VS_CURRENCY = "usd"
DB_PATH = os.path.join("data", "crypto_prices.db")

def fetch_current_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": ",".join(COINS),
        "vs_currencies": VS_CURRENCY
    }
    response = requests.get(url, params=params)
    data = response.json()
    records = []
    timestamp = datetime.now(timezone.utc).isoformat()
    for coin in COINS:
        records.append({
            "coin": coin,
            "price": data[coin][VS_CURRENCY],
            "timestamp": timestamp
        })
    return pd.DataFrame(records)

def save_to_db(df):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            coin TEXT,
            price REAL,
            timestamp TEXT
        )
    """)
    df.to_sql("prices", conn, if_exists="append", index=False)
    conn.close()

if __name__ == "__main__":
    df = fetch_current_prices()
    print(df)
    save_to_db(df)
    print("Data saved to database")