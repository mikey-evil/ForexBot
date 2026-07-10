import MetaTrader5 as mt5

def bullish(candle):
    return candle['close'] > candle['open']

def bearish(candle):
    return candle['close'] < candle['open']