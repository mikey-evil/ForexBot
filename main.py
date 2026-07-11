from market_data import *
from indicators import *
from strategy import *
from structure import *
from liquidity import *

if not connect():
    quit()

symbol = "EURUSD"

candles = get_candles(symbol, mt5.TIMEFRAME_M5, 100)

df = calculate_ema(candles, 20)
df = calculate_rsi(df)

last_close = df["close"].iloc[-1]
last_ema = df["EMA"].iloc[-1]
last_rsi = df["RSI"].iloc[-1]

trend = "🟢 UP" if last_close > last_ema else "🔴 DOWN"

if last_rsi > 70:
    rsi_status = "🔴 Overbought"
elif last_rsi < 30:
    rsi_status = "🟢 Oversold"
else:
    rsi_status = "🟡 Neutral"

signal = get_signal(last_close, last_ema, last_rsi)

support = get_support(df)
resistance = get_resistance(df)

swing_highs = find_swing_highs(df)
swing_lows = find_swing_lows(df)

bos = detect_bos(df)
choch = detect_choch(df)

liquidity = detect_liquidity(df)

print("=" * 60)
print("FOREX BOT")
print("=" * 60)

print(f"Symbol        : {symbol}")
print(f"Trend         : {trend}")
print(f"RSI           : {last_rsi:.2f}")
print(f"RSI Status    : {rsi_status}")
print(f"Signal        : {signal}")
print(f"Support       : {support}")
print(f"Resistance    : {resistance}")

print()

if swing_highs:
    print(f"Swing High    : {swing_highs[-1][1]}")

if swing_lows:
    print(f"Swing Low     : {swing_lows[-1][1]}")

print(f"BOS           : {bos}")
print(f"CHoCH         : {choch}")
print(f"Liquidity     : {liquidity}")

disconnect()