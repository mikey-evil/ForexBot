def get_signal(close, ema, rsi):

    if close > ema and rsi > 50:
        return "🟢 BUY"

    elif close < ema and rsi < 50:
        return "🔴 SELL"

    else:
        return "⚪ NO TRADE"