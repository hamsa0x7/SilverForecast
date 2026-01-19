# Silver Price Directional Forecasting

**Author:** JoJo  
**Goal:** Predict silver price direction (up/down) for the next 30 days with >60% accuracy using Machine Learning.

---

## Project Overview

This project implements a production-ready time series forecasting pipeline to analyze 10 years of silver futures data (2016-2026). The goal is to assist in trading decisions by predicting daily price movements with high directional accuracy.

**Key Features:**
- **Data Source:** Daily COMEX Silver Futures (SI=F) from Yahoo Finance.
- **Methodology:** Comparative analysis of ARIMA, Prophet, and LSTM (Deep Learning) models.
- **Target Metric:** Directional Accuracy (Target: >60%).
- **Constraints:** Optimized for real-time inference (<1s latency).

---

## Repository Structure

The project follows a modular Data Science structure:

```
SilverForecast/
├── documents/           # Detailed reports (Model Card, Data Quality, EDA)
├── data/                # Data storage (Raw & Processed)
├── notebooks/           # Jupyter notebooks for analysis and experimentation
├── src/                 # Source code for features and modeling
└── models/              # Saved model binary artifacts
```

## Key Deliverables

1.  **Analysis Notebook:** [`notebooks/complete_ml_pipeline.ipynb`](notebooks/complete_ml_pipeline.ipynb) - Contains the full end-to-end pipeline including EDA, feature engineering, and model training.
2.  **Model Card:** [`documents/ModelCard.md`](documents/ModelCard.md) - Constitutional documentation defining model scope, limitations, and performance metrics.
3.  **Baseline Results:** Achieved **53.60%** accuracy with a naive persistence baseline, establishing the floor for ML model performance.

---

## Getting Started

1.  Clone the repository.
2.  Install dependencies (e.g., `pandas`, `sklearn`, `prophet`, `tensorflow`).
3.  Run the pipeline notebook:
    ```bash
    jupyter notebook notebooks/complete_ml_pipeline.ipynb
    ```

---

## License
MIT


