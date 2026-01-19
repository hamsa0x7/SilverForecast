# Phase 0: Problem & Data Understanding

**Date:** 2026-01-17  
**Tier:** Production ML  
**Duration:** 30 minutes

---

## Problem

Predict silver price **direction** (up/down) for the next 30 days using 10 years of historical data from Yahoo Finance.

---

## Success Criteria

- **Primary Metric:** Directional Accuracy > 60%
- **Secondary:** Beat baselines (last-value ~50%, moving average ~55%)
- **Comparison:** Outperform dataset's existing 2026 forecast

---

## Data

- **Source:** Kaggle - "Silver Prices: 10-Year Data & 2026 Forecast"
- **URL:** https://www.k aggle.com/datasets/muhammadaammartufail/silver-prices-10-year-data-and-2026-forecast
- **Size:** ~2,610 daily prices (Jan 2016 - Jan 2026)
- **Features:** Open, High, Low, Close, Volume
- **Target:** Direction (binary: up/down) - derived from Close price

---

## Constraints

- **Latency:** Real-time predictions (< 1 second)
- **Interpretability:** Must explain predictions (SHAP, attention weights)
- **Compute:** Single GPU/CPU (educational budget)
- **Purpose:** Educational/portfolio project

---

## Decisions Made

### Model Candidates
1. **ARIMA** - Classic, interpretable, fast
2. **Prophet** - Seasonality handling, explainable
3. **LSTM with Attention** - Best accuracy, attention provides interpretability

**Strategy:** Train all 3, compare on validation set, select best.

### Evaluation
- **Primary:** Directional Accuracy
- **Secondary:** Precision, Recall, F1
- **Business:** ROI simulation, Sharpe ratio

### Data Split
- Train: 70% (2016-2022)
- Validation: 15% (2023)
- Test: 15% (2024-2026)

**No shuffling** - time series order preserved.

---

## Next Steps

1. **Phase 0.5:** Git + DVC setup
2. **Phase 1:** Download Kaggle dataset, data quality assessment
3. **Phase 2:** EDA - trends, seasonality, outliers
4. **Phase 3:** Feature engineering (technical indicators, lag features)
