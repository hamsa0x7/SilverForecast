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
✅ **Phase 0.5:** Git Setup Complete  
✅ **Phase 1:** Data Collection Complete  
✅ **Phase 2-4:** EDA & Baseline Complete  
✅ **Phase 5-9:** Full ML Pipeline Complete (Notebook)

---

## Constitutional Document

See [`documents/ModelCard.md`](documents/ModelCard.md) for complete specifications.

## Key Results

- **Baseline:** 53.60% (Naive Persistence)
- **Target:** >60% Directional Accuracy
- **Full Pipeline:** See [`notebooks/complete_ml_pipeline.ipynb`](notebooks/complete_ml_pipeline.ipynb)

---

## Next Steps

Project is **COMPLETE**. 

To run the pipeline:
1. Open `notebooks/complete_ml_pipeline.ipynb`
2. Run all cells to execute training and validation

