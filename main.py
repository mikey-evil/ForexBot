from market_data import *
from indicators import *
from strategy import *
from structure import *
from liquidity import *

# Connect MT5
if not connect():
    quit()

symbol = "EURUSD"

# Get Market Data
df = get_candles(symbol, mt5.TIMEFRAME_M5, 100)

if df is None:
    print("❌ Failed to get candles")
    disconnect()
    quit()

# Indicators
df = calculate_ema(df, 20)
df = calculate_rsi(df)
df = calculate_atr(df)

# Latest Values
last_close = df["close"].iloc[-1]
last_ema = df["EMA"].iloc[-1]
last_rsi = df["RSI"].iloc[-1]
last_atr = df["ATR"].iloc[-1]

# Trend
trend = "🟢 UP" if last_close > last_ema else "🔴 DOWN"

# RSI Status
if last_rsi > 70:
    rsi_status = "🔴 Overbought"
elif last_rsi < 30:
    rsi_status = "🟢 Oversold"
else:
    rsi_status = "🟡 Neutral"

# Strategy
signal = get_signal(last_close, last_ema, last_rsi)

# Structure
support = get_support(df)
resistance = get_resistance(df)

swing_highs = find_swing_highs(df)
swing_lows = find_swing_lows(df)

bos = detect_bos(df)
choch = detect_choch(df)
liquidity = detect_liquidity(df)

# Output
print("=" * 60)
print("FOREX BOT")
print("=" * 60)

print(f"Symbol        : {symbol}")
print(f"Trend         : {trend}")
print(f"Close Price   : {last_close}")
print(f"EMA(20)       : {last_ema:.5f}")
print(f"RSI           : {last_rsi:.2f}")
print(f"ATR           : {last_atr:.5f}")
print(f"RSI Status    : {rsi_status}")
print(f"Signal        : {signal}")
print()

print(f"Support       : {support}")
print(f"Resistance    : {resistance}")

print()

if swing_highs:
    print(f"Swing High    : {swing_highs[-1][1]}")

if swing_lows:
    print(f"Swing Low     : {swing_lows[-1][1]}")

print()

print(f"BOS           : {bos}")
print(f"CHoCH         : {choch}")
print(f"Liquidity     : {liquidity}")

disconnect()