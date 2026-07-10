import MetaTrader5 as mt5

def connect():
    if not mt5.initialize():
        print("❌ MT5 Connection Failed")
        return False

    print("✅ MT5 Connected")
    return True


def disconnect():
    mt5.shutdown()


def get_last_candle(symbol):

    candle = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 0, 1)

    if candle is None or len(candle) == 0:
        return None

    return candle[0]
def get_candles(symbol, timeframe, count):

    candles = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)

    if candles is None or len(candles) == 0:
        return None

    return candles