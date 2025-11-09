# features_engineering.py
import numpy as np
import pandas as pd

def compute_RSI(series, period=14):
    delta = series.diff()
    up = delta.clip(lower=0).rolling(window=period).mean()
    down = -delta.clip(upper=0).rolling(window=period).mean()
    rs = up / down
    return 100 - (100 / (1 + rs))

def create_features(df):
    df = df.copy()
    df['returns'] = df['Close'].pct_change()
    df['SMA_10'] = df['Close'].rolling(10).mean()
    df['SMA_50'] = df['Close'].rolling(50).mean()
    df['MACD'] = df['Close'].ewm(span=12, adjust=False).mean() - df['Close'].ewm(span=26, adjust=False).mean()
    df['RSI'] = compute_RSI(df['Close'], period=14)
    df = df.dropna().reset_index(drop=True)
    return df
