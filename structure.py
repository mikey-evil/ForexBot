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
            swing_highs.append(df["high"].iloc[i])

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
            swing_lows.append(df["low"].iloc[i])

    return swing_lows