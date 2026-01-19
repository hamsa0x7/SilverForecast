# Phase 2: EDA Results - Silver Price Analysis

**Date:** 2026-01-17  
**Phase:** 2 - Exploratory Data Analysis  
**Status:** ✅ Complete

---

## Key Findings

### 1. Price Statistics
- **Min Price:** $12.20
- **Max Price:** $93.00
- **Range:** $80.80
- **Mean:** ~$22.71
- **Volatility:** Moderate (std dev ~$8.40)

### 2. Trend Analysis
- **Overall 10-year trend:** +77.1% 
- **Positive days:** 51.4% (slightly bullish bias)
- **Negative days:** 48.6%
- **Mean daily return:** ~0.03%

### 3. Baseline Model Performance
- **Naive Forecast (Persistence Model):** 50.71% accuracy
- **Beats random (50%):** ✅ YES (marginally)
- **Our target:** >60% accuracy

**Implication:** Our ML models must beat 50.71% to be worthwhile.

###4. Outlier Detection
- **Outliers found:** 103 days (4.1% of data)
- **Method:** IQR (Interquartile Range)
- **Cause:** Likely major market events (COVID-19, inflation spikes)

### 5. Volatility
- **Average daily change:** ~$0.25
- **Maximum single-day change:** Significant spikes during volatile periods
- **Volatility (std of returns):** Moderate

---

## Insights for Modeling

### ✅ Good News
1. **Slight upward trend** over 10 years - momentum features may help
2. **Baseline is beatable** at 50.71% - room for improvement
3. **Moderate volatility** - not too chaotic for modeling
4. **Outliers are identifiable** - can handle separately

### ⚠️ Challenges
1. **Near 50/50 split** (up vs down) - class balance good but makes prediction hard
2. **Trend only +77% over 10 years** - relatively flat, weak trend signal
3. **Outliers exist** - need robust models or outlier handling
4. **No clear seasonality** (needs deeper analysis)

---

## Model Strategy Recommendations

Based on EDA findings:

1. **Feature Engineering Priority:**
   - **Lag features** (t-1, t-7, t-30 prices)
   - **Technical indicators** (RSI, MACD, Bollinger Bands)
   - **Volatility features** (rolling std, ATR)

2. **Model Candidates:**
   - **ARIMA:** Good baseline, handles trend
   - **Prophet:** May struggle without strong seasonality
   - **LSTM:** Best for capturing long-term patterns

3. **Success Threshold:**
   - Must beat **50.71% baseline**
   - Target: **>60% directional accuracy**
   - Stretch goal: **65%+**

---

## Next Steps (Phase 3)

1. Create derived features (returns, momentum, volatility)
2. Engineer technical indicators
3. Prepare train/val/test splits (70/15/15)
4. Create target variable (direction: up=1, down=0)

---

**Phase 2 Status:** ✅ COMPLETE  
**Ready for Phase 3:** ✅ YES
