import pandas as pd

def calculate_ema(candles, period=20):
    df = pd.DataFrame(candles)

    df["EMA"] = df["close"].ewm(span=period, adjust=False).mean()

    return df
from ta.momentum import RSIIndicator

def calculate_rsi(df, period=14):

    rsi = RSIIndicator(close=df["close"], window=period)

    df["RSI"] = rsi.rsi()

    return df