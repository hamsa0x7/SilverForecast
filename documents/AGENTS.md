# AGENTS.md - Silver Forecasting Project Memory

**Project:** Silver Price Directional Forecasting  
**Tier:** Production ML  
**Status:** Phase 0 Complete  
**Created:** 2026-01-17

---

## Project Context

### Problem
Predict whether silver price will go **up** or **down** in the next 30 days using 10 years of historical futures data.

### Data
- **Source:** Kaggle (Yahoo Finance API)
- **Ticker:** SI=F (COMEX Silver Futures)
- **Size:** ~2,610 daily prices (2016-2026)
- **Target:** Binary direction (up=1, down=0)

### Success Criteria
- **Metric:** Directional Accuracy > 60%
- **Beat baseline:** Last-value (~50%), Moving Average (~55%)
- **Beat existing:** Dataset's 2026 forecast

---

## Key Decisions

### Model Selection
- **Chosen:** Train 3 models (ARIMA, Prophet, LSTM+Attention)
- **Why:** Test classical vs modern, balance speed/accuracy/interpretability
- **Rejected:** Random Forest (no temporal order), Transformer (dataset too small)

### Feature Engineering
- **Planned Features:**
  - Technical indicators: RSI, MACD, Bollinger Bands
  - Lag features: t-1, t-7, t-30
  - Momentum, Volatility, Trend

### Constraints
- Real-time inference (< 1s)
- Interpretability required (SHAP/attention)
- Single GPU/CPU budget

---

## Experiment Log

| Experiment | Phase | Status | Notes |
|------------|-------|--------|-------|
| Phase 0 | Problem Definition | ✅ Complete | Model Card created |
| Phase 0.5 | Git Setup | ⏳ Pending | Next step |
| Phase 1 | Data Collection | ⏳ Pending | Download from Kaggle |

---

## Current Status

**Phase:** 0 (Complete)  
**Next Steps:**
1. Initialize Git + DVC
2. Download Kaggle dataset
3. Data quality assessment

---

## Known Issues
- None yet (project just started)

---

## Future Work
- Add external features (gold price, USD index, interest rates)
- Test ensemble methods (combine ARIMA + LSTM)
- Real-time data pipeline for continuous retraining

---

**Constitutional Document:** See `documents/ModelCard.md` for complete specs.
