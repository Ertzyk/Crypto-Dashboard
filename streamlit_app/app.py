import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
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
st.subheader("Price Chart")
if not df.empty:
    selected_coin = st.selectbox("Choose a coin to display:", df['coin'].unique())
    coin_df = df[df['coin'] == selected_coin]
    fig, ax = plt.subplots()
    ax.plot(pd.to_datetime(coin_df['timestamp']), coin_df['price'], marker='o')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Price (USD)')
    ax.set_title(f'{selected_coin.capitalize()} Price Over Time')
    plt.xticks(rotation = 45)
    st.pyplot(fig)
else:
    st.write("No data")