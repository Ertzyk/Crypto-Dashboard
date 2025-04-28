# Crypto Dashboard

A simple cryptocurrency dashboard that fetches live crypto prices, saves them in a local database, and displays visual charts using Streamlit.

---

## 🚀 Features

- Fetches live prices of popular coins from CoinGecko API
- Saves historical price data into a local SQLite database
- Streamlit frontend with:
  - Live price tables
  - Interactive price charts (matplotlib)
  - Dropdown filter to select different coins
- Unit tested with pytest ✅

---

## 🛠️ Technologies Used

- Python 3
- Streamlit
- SQLite (sqlite3)
- pandas
- matplotlib
- requests
- pytest

---

## 📦 Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/crypto-dashboard.git
    cd crypto-dashboard
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate   # On Windows
    # or
    source venv/bin/activate  # On Mac/Linux
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 How to Run

1. Fetch current prices manually:
    ```bash
    python scripts/fetch_prices.py
    ```

2. Start the Streamlit app:
    ```bash
    streamlit run streamlit_app/app.py
    ```