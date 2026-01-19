# Phase 3: Feature Engineering Complete

**Date:** 2026-01-17  
**Phase:** 3 - Feature Engineering  
**Status:** ✅ Complete

---

## Features Created

### Total: 13 Features

1. **Price-based (1)**
   - `price`: Closing price

2. **Derived Features (2)**
   - `return`: Daily return (%)
   - `momentum`: 5-day price momentum (%)

3. **Technical Indicators (4)**
   - `sma_5`: 5-day Simple Moving Average
   - `sma_20`: 20-day Simple Moving Average
   - `sma_50`: 50-day Simple Moving Average
   - `rsi`: 14-period Relative Strength Index

4. **Volatility Features (2)**
   - `bb_distance`: Distance from Bollinger Band middle (in std devs)
   - `volatility`: 30-day rolling standard deviation

5. **Lag Features (3)**
   - `lag_1`: Price 1 day ago
   - `lag_7`: Price 7 days ago (weekly pattern)
   - `lag_30`: Price 30 days ago (monthly pattern)

6. **Target Variable (1)**
   - `target`: Direction (1=up, 0=down)

---

## Target Distribution

- **Up days (1):** 51.4%
- **Down days (0):** 48.6%
- **Balance:** ✅ Good (near 50/50 split)

**Implication:** No class imbalance issues - models won't be biased toward one class.

---

## Output

**File:** `data/processed/silver_features.csv`  
**Rows:** 2,513  
**Columns:** 14 (13 features + 1 target)

**Format:**
```csv
date,price,return,sma_5,sma_20,sma_50,rsi,bb_distance,momentum,volatility,lag_1,lag_7,lag_30,target
2016-01-19,14.11,0.0,0.0,0.0,0.0,50.0,0.0,0.0,0.0,0.0,0.0,0.0,1
...
```

---

## Key Insights

### ✅ Good Features for Modeling

1. **Multi-timeframe indicators:** 5, 20, 50-day SMAs capture short/medium/long trends
2. **RSI:** Captures overbought/oversold conditions
3. **Momentum:** Captures price acceleration
4. **Volatility:** Identifies high/low risk periods
5. **Lag features:** Provide historical context

### 📊 Feature Engineering Strategy

- **Trend following:** SMA features help identify uptrend/downtrend
- **Mean reversion:** RSI + Bollinger detect extremes
- **Momentum:** Captures short-term price acceleration
- **Memory:** Lag features give models "hindsight"

---

## Next Steps (Phase 4)

1. Load processed features from CSV
2. Split data: Train (70%), Validation (15%), Test (15%)
3. Train baseline model (naive persistence)
4. Establish threshold to beat: >50.71%

---

**Phase 3 Status:** ✅ COMPLETE  
**Ready for Phase 4:** ✅ YES  
**Processed Data:** `data/processed/silver_features.csv`
