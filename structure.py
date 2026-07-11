def get_support(df):
    return df["low"].min()


def get_resistance(df):
    return df["high"].max()


def find_swing_highs(df):
    swing_highs = []

    for i in range(2, len(df) - 2):
        if (
            df["high"].iloc[i] > df["high"].iloc[i - 1]
            and df["high"].iloc[i] > df["high"].iloc[i - 2]
            and df["high"].iloc[i] > df["high"].iloc[i + 1]
            and df["high"].iloc[i] > df["high"].iloc[i + 2]
        ):
            swing_highs.append((i, df["high"].iloc[i]))

    return swing_highs


def find_swing_lows(df):
    swing_lows = []

    for i in range(2, len(df) - 2):
        if (
            df["low"].iloc[i] < df["low"].iloc[i - 1]
            and df["low"].iloc[i] < df["low"].iloc[i - 2]
            and df["low"].iloc[i] < df["low"].iloc[i + 1]
            and df["low"].iloc[i] < df["low"].iloc[i + 2]
        ):
            swing_lows.append((i, df["low"].iloc[i]))

    return swing_lows


def detect_bos(df):

    highs = find_swing_highs(df)
    lows = find_swing_lows(df)

    last_close = df["close"].iloc[-1]

    if len(highs) >= 2:
        if last_close > highs[-2][1]:
            return "🟢 Bullish BOS"

    if len(lows) >= 2:
        if last_close < lows[-2][1]:
            return "🔴 Bearish BOS"

    return "⚪ No BOS"


def detect_choch(df):

    highs = find_swing_highs(df)
    lows = find_swing_lows(df)

    if len(highs) < 2 or len(lows) < 2:
        return "⚪ No CHoCH"

    last_close = df["close"].iloc[-1]

    latest_high = highs[-1][1]
    latest_low = lows[-1][1]

    if last_close > latest_high:
        return "🟢 Bullish CHoCH"

    if last_close < latest_low:
        return "🔴 Bearish CHoCH"

    return "⚪ No CHoCH"