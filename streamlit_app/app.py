import streamlit as st
import sqlite3
import pandas as pd
import os

DB_PATH = os.path.join("data", "crypto_prices.db")

st.title("Crypto Dashboard")

@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM prices", conn)
    conn.close()
    return df

df = load_data()
st.subheader("Latest Prices")
st.dataframe(df)