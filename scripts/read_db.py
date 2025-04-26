import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join("data", "crypto_prices.db")

def read_from_db():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM prices", conn)
    conn.close()
    return df

if __name__ == "__main__":
    df = read_from_db()
    print(df)