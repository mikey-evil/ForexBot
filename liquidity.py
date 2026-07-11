def detect_liquidity(df):

    last_high = df["high"].iloc[-1]
    prev_high = df["high"].iloc[-2]

    last_low = df["low"].iloc[-1]
    prev_low = df["low"].iloc[-2]

    if last_high > prev_high:
        return "🟢 Buy Side Liquidity Taken"

    elif last_low < prev_low:
        return "🔴 Sell Side Liquidity Taken"

    else:
        return "⚪ No Liquidity Sweep"