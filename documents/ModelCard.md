# Model Card: Silver Price Directional Forecasting

**Status:** Constitutional Source of Truth  
**Version:** 1.0  
**Tier:** Production ML  
**Date:** 2026-01-17  
**Research Conducted:** Yes

---

## 0. Executive Summary

### Problem at a Glance
- **Problem:** Predict silver price direction (up/down) for the next 30 days
- **Data:** 10 years of daily silver futures prices (2016-2026) from Yahoo Finance
- **Model:** Time series forecasting with interpretability (ARIMA, Prophet, or LSTM with attention)
- **Performance Target:** Directional accuracy > 60% (beat random 50%)
- **Status:** Phase 0 Complete - Ready for Data Assessment

### Key Findings (Pending)
- [To be filled after EDA]
- [Trend analysis results]
- [Seasonality patterns]

### Next Steps
- Phase 0.5: Git setup with DVC for data versioning
- Phase 1: Download Kaggle dataset, assess quality

---

## 1. Problem Definition

### 1.1 Business/Research Question
**Primary Question:** Can we predict the direction of silver price movement (up/down) for the next 30 days with better than random accuracy?

**Secondary Questions:**
- What features/patterns drive silver price movements?
- How does our model compare to the existing 2026 forecast in the dataset?
- Can we explain WHY the model predicts certain directions?

### 1.2 Success Criteria

**Primary Goal:**
- **Directional Accuracy > 60%** (significantly better than random 50%)
- **Metric:** % of correct up/down predictions on test set

**Secondary Goals:**
- **Interpretability:** Model can explain top 3 factors for each prediction
- **Beat Baseline:** Outperform naive forecast (last-value, moving average)
- **Beat Existing Forecast:** Compare against dataset's 2026 predictions

### 1.3 Constraints

- **Latency:** Real-time predictions required (< 1 second inference time)
- **Interpretability:** Must explain predictions (SHAP, feature importance, or attention weights)
- **Compute:** Train on single GPU or CPU (educational project budget)
- **Privacy:** No concerns (public market data)

---

## 2. Data Overview

### 2.1 Data Sources
- **Source 1:** Kaggle - "Silver Prices: 10-Year Data & 2026 Forecast"
  - URL: https://www.kaggle.com/datasets/muhammadaammartufail/silver-prices-10-year-data-and-2026-forecast
  - Provider: Yahoo Finance API (yfinance)
  - Ticker: SI=F (COMEX Silver Futures)

### 2.2 Dataset Characteristics
- **Samples:** ~2,610 days (10 years of daily data, Jan 2016 - Jan 2026)
- **Features:** Open, High, Low, Close, Volume (typical OHLCV data)
- **Target Variable:** Direction (binary: 1=up, 0=down) - **derived from Close price**
- **Time Period:** January 2016 - January 2026

### 2.3 Data Quality Summary
- **Missing Values:** [To be assessed in Phase 1]
- **Outliers:** [To be detected in Phase 2]
- **Class Imbalance:** [To be calculated - likely near 50/50 for directional]

---

## 3. Evaluation Metrics

### 3.1 Primary Metric
**Metric:** **Directional Accuracy**  
**Formula:** (Correct Up + Correct Down) / Total Predictions  
**Why:** For trading/investment decisions, knowing the direction is more valuable than exact price. A 60% accuracy can be profitable.

### 3.2 Secondary Metrics
- **Precision (Up):** How often "up" predictions are correct (avoid false signals)
- **Recall (Up):** How many actual "up" days we caught (opportunity capture)
- **F1 Score:** Balance precision/recall
- **Comparison to Baseline:** % improvement over naive forecast

### 3.3 Business KPIs
- **ROI Simulation:** If used in a simple trading strategy (buy on "up" prediction, sell on "down"), what's the return?
- **Sharpe Ratio:** Risk-adjusted return
- **Maximum Drawdown:** Worst losing streak

---

## 4. Baseline Performance

### 4.1 Simple Baselines
**Method 1:** **Last-Value Persistence** ("tomorrow will be same direction as today")  
**Expected Performance:** ~50% (random walk hypothesis)

**Method 2:** **Moving Average Crossover** (if 5-day MA > 20-day MA, predict "up")  
**Expected Performance:** ~55% (common technical indicator)

**Method 3:** **Dataset's Existing 2026 Forecast**  
**Expected Performance:** Unknown - will compare directly

**Purpose:** Any ML model must beat at least 55% to be useful.

---

## 5. Model Selection Rationale

### 5.1 Chosen Models (3 Candidates)
**Algorithm 1:** **ARIMA** (AutoRegressive Integrated Moving Average)  
**Why:** Classic time series, interpretable, fast  
**Pros:** No ML complexity, explainable  
**Cons:** Assumes linearity, may miss complex patterns

**Algorithm 2:** **Prophet** (Facebook's forecasting tool)  
**Why:** Handles seasonality well, interpretable trend/seasonality decomposition  
**Pros:** Built-in interpretability, robust to missing data  
**Cons:** May overfit on short-term noise

**Algorithm 3:** **LSTM with Attention** (Deep Learning)  
**Why:** Captures long-term dependencies, attention mechanism provides interpretability  
**Pros:** Best accuracy potential, attention weights show "what the model looks at"  
**Cons:** Harder to train, needs more data

### 5.2 Alternatives Considered
| Model | Pros | Cons | Rejected Why |
|-------|------|------|--------------|
| **Random Forest** | Fast, feature importance | Not designed for time series | Ignores temporal order |
| **XGBoost** | High accuracy | No native time series support | Need manual feature engineering |
| **Transformer** | State-of-art | Overkill for 10 years of data | Dataset too small |

### 5.3 Trade-offs
- **Speed vs Accuracy:** ARIMA (fast) vs LSTM (accurate)
- **Interpretability vs Performance:** Prophet (explainable) vs LSTM (black box but attention helps)
- **Complexity vs Maintainability:** ARIMA (simple) vs LSTM (needs tuning)

**Decision:** Train all 3, compare on validation set, select best for production.

---

## 6. Feature Strategy

### 6.1 Key Features (To Be Engineered)
1. **Price-based:** Daily return, Log return, Price volatility (rolling std)
2. **Technical Indicators:** RSI, MACD, Bollinger Bands, Moving Averages (5, 20, 50-day)
3. **Temporal:** Day of week, Month (seasonality check)
4. **Lag Features:** Price from t-1, t-7, t-30 (previous day, week, month)
5. **Volume:** Trading volume, volume change

### 6.2 Feature Engineering
**Transformations:**
- Log transformation of price (stabilize variance)
- Rolling window statistics (mean, std, min, max)
- Differencing (make series stationary for ARIMA)

**Created Features:**
- **Momentum:** (Close_t - Close_t-5) / Close_t-5
- **Volatility:** Rolling 30-day standard deviation
- **Trend:** Linear regression slope over last 30 days

---

## 7. Training Details

### 7.1 Hyperparameters (To Be Tuned)
**ARIMA:**
```
p: [1, 2, 3]  # AR order
d: [0, 1]     # Differencing
q: [1, 2, 3]  # MA order
```

**Prophet:**
```
changepoint_prior_scale: [0.05, 0.1, 0.5]
seasonality_mode: ['additive', 'multiplicative']
```

**LSTM:**
```
hidden_size: [64, 128]
num_layers: [2, 3]
dropout: [0.2, 0.3]
learning_rate: [0.001, 0.0001]
```

### 7.2 Data Split
- **Train:** 70% (first 7 years: 2016-2022)
- **Validation:** 15% (2023)
- **Test:** 15% (2024-2026)

**Why:** Time series split (no shuffling - preserves temporal order)

### 7.3 Compute Requirements
- **Hardware:** CPU-only for ARIMA/Prophet, GPU (single RTX 3060) for LSTM
- **Training Time:** ARIMA (seconds), Prophet (minutes), LSTM (1-2 hours)

---

## 8. Validation Results (After Training)

### 8.1 Test Set Performance
**Primary Metric:** [Directional Accuracy] = [TBD]%  
**Secondary Metrics:**
- Precision: [TBD]
- Recall: [TBD]
- F1 Score: [TBD]

### 8.2 Confusion Matrix
[To be filled after Phase 6]

### 8.3 Failure Modes
**Where the model struggles:**
- [e.g., "During sudden market shocks (COVID-19 crash)"]
- [e.g., "Low volume days with high noise"]

---

## 9. Fairness & Ethics

### 9.1 Protected Attributes
**N/A** - This is market data, no demographic bias concerns.

### 9.2 Ethical Considerations
- **Market Manipulation:** Model should not be used for pump-and-dump schemes
- **Investment Risk:** Predictions are not financial advice, users should understand risk
- **Educational Purpose:** This is a portfolio/learning project, not professional trading advice

---

## 10. Deployment Plan

### 10.1 Serving Infrastructure
**Platform:** FastAPI REST API (Docker container)  
**Latency Target:** < 1 second (real-time prediction)  
**Throughput:** 10 requests/sec (low volume, educational)

**Deployment Flow:**
1. User sends date → API returns prediction (up/down) + explanation
2. Model loaded in memory (lightweight ARIMA/Prophet) or GPU (LSTM)

### 10.2 Monitoring Metrics
- **Model Performance:** Track rolling 7-day directional accuracy
- **Data Drift:** Monitor if recent price distribution shifts significantly
- **Concept Drift:** If accuracy drops below 55%, trigger retraining

### 10.3 Retraining Strategy
**Trigger:** Performance drops below 55% for 30 consecutive days  
**Frequency:** Monthly retraining with latest data (rolling window)

---

## 11. Risks & Limitations

### 11.1 Known Limitations
- **Market Unpredictability:** Silver prices affected by macroeconomic factors (USD strength, inflation, geopolitical events) that model may not capture
- **Limited Features:** Only price/volume data, no external features (gold price, USD index, interest rates)
- **10-Year Horizon:** Model trained on 2016-2026 data may not generalize to different market regimes

### 11.2 Data Drift Risks
**Potential Issues:**
- **Regime Change:** If silver enters a new bull/bear market, model may fail
- **Volume Anomalies:** If trading volume drops significantly, predictions may be noisier

### 11.3 Model Degradation Triggers
**When to escalate:**
- Directional accuracy < 50% for 14 days (worse than random)
- 3 consecutive days of >5% price swings (high volatility regime)
- User feedback: predictions consistently wrong

---

## 12. Versioning & Approval

- **Model Version:** 1.0 (initial)
- **Date Trained:** [2026-01-17 - TBD after Phase 5]
- **Data Version:** Kaggle dataset (downloaded 2026-01-17)
- **Code Version:** [Git commit hash - TBD after Phase 0.5]
- **Approved By:** JoJo (Educational/Portfolio Project)

---

**This Model Card is the constitutional source of truth for the project. All experiments, training, and deployment decisions must conform to it.**
