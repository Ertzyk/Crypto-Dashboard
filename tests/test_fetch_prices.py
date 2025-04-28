import pandas as pd
from scripts.fetch_prices import fetch_current_prices

def test_fetch_prices_structure():
    df = fetch_current_prices()
    assert isinstance(df, pd.DataFrame)
    assert "coin" in df.columns
    assert "price" in df.columns
    assert "timestamp" in df.columns
    assert not df.empty