import pandas as pd
from scripts.fetch_prices import fetch_current_prices

def test_prices_are_positive():
    df = fetch_current_prices()
    assert (df['price'] > 0).all(), "Found non-positive price(s)!"