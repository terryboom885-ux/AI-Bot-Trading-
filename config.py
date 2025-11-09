# config.py
CONFIG = {
    "market": "stocks",
    "assets": ["AAPL","MSFT","NVDA","SPY"],
    "data_start": "2019-01-01",
    "data_end": None,               # None -> today
    "lookback_window": 60,          # how many candles to require before signals
    "train_test_split": 0.8,
    "risk_per_trade": 0.02,         # fraction of capital risked per trade
    "initial_capital": 10000.0,
    "take_profit_pct": 0.015,       # 1.5% TP relative to entry
    "stop_loss_pct": 0.01,          # 1.0% SL relative to entry
    "ai_model": "xgboost",
    "min_confidence": 0.7
}
