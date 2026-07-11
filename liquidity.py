def detect_liquidity(df):

    last_high = df["high"].iloc[-1]
    previous_high = df["high"].iloc[-2]

    last_low = df["low"].iloc[-1]
    previous_low = df["low"].iloc[-2]

    if last_high > previous_high:
        return "🟢 Buy Side Liquidity"

    elif last_low < previous_low:
        return "🔴 Sell Side Liquidity"

    else:
        return "⚪ No Liquidity Sweep"