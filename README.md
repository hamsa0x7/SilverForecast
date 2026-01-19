# Silver Price Directional Forecasting

**Status:** Phase 0 Complete ✅  
**Tier:** Production ML  
**Goal:** Predict silver price direction (up/down) for next 30 days with >60% accuracy

---

## Quick Start

This project uses the **Agentic AI Data Science Playbook** to build a production-ready time series forecasting model.

**Key Info:**
- 📊 Data: 10 years of daily silver futures (2016-2026) from Yahoo Finance
- 🎯 Metric: Directional Accuracy > 60%
- 🧠 Models: ARIMA, Prophet, LSTM with Attention
- ⚡ Constraint: Real-time predictions (<1s), Interpretable

---

## Project Structure

```
SilverForecast/
├── documents/           # Model Card, AGENTS.md, experiment logs
├── data/               # raw, processed, external
├── notebooks/          # EDA, feature engineering, modeling
├── src/                # Production code
├── models/             # Trained model artifacts
├── results/            # Figures, tables, reports
└── README.md
```

---

## Status

✅ **Phase 0:** Problem Definition Complete  
⏳ **Phase 0.5:** Git Setup (Next)  
⏳ **Phase 1:** Data Collection  
⏳ **Phase 2-9:** Full ML Pipeline

---

## Constitutional Document

See [`documents/ModelCard.md`](documents/ModelCard.md) for complete specifications.

---

## Next Steps

1. Initialize Git + DVC for data versioning
2. Download Kaggle dataset
3. Run EDA (trend, seasonality, stationarity analysis)
4. Feature engineering (technical indicators)
5. Train baseline models
