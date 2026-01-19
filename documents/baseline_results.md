# Phase 4: Baseline Model Results

**Date:** 2026-01-17  
**Phase:** 4 - Baseline Model & Data Split  
**Status:** ✅ Complete

---

## Data Split (Time Series)

**No shuffling** - preserves temporal order

- **Train:** 1,759 samples (70%) - 2016 to ~2022
- **Validation:** 377 samples (15%) - ~2023
- **Test:** 377 samples (15%) - ~2024-2026

**Total:** 2,513 samples

---

## Baseline Model Results

### Baseline 1: Naive Persistence
**Strategy:** "Tomorrow will be same direction as today"

- **Train:** 53.80%
- **Validation:** 54.24%
- **Test:** **53.60%** ⭐

### Baseline 2: Moving Average Crossover
**Strategy:** "If SMA5 > SMA20, predict UP"

- **Train:** 51.05%
- **Validation:** 50.40%
- **Test:** **51.30%**

---

## Performance Threshold

**Best Baseline (Test):** 53.60%  
**Random Chance:** 50.00%  
**Our Target:** >60.00%

### Gap Analysis
- **Gap to target:** 6.4 percentage points
- **Required improvement:** 11.94% relative improvement over baseline

**Challenge:** Need to add 6.4 points to hit our >60% target!

---

## Insights

### ✅ Good News
1. **Baseline beats random:** 53.60% > 50% (✅)
2. **Consistent across splits:** Train/Val/Test all ~53-54%
3. **Beatable threshold:** 6.4 points is achievable with ML

### 📊 What This Means
- **Naive persistence works okay** (slight momentum effect in silver prices)
- **Technical indicators alone don't help much** (MA crossover only 51.3%)
- **ML models need to capture non-linear patterns** to beat 53.60%

---

## Model Strategy for Phase 5

To beat 53.60%, our models must:

1. **Capture longer-term patterns** (LSTM's strength)
2. **Use all 13 features** (not just price momentum)
3. **Find non-linear relationships** (RSI + Volatility interactions)

**Model Priorities:**
1. **ARIMA:** May struggle (linear), target: 54-56%
2. **Prophet:** Better with features, target: 56-58%
3. **LSTM:** Best chance, target: 60-65%

---

## Next Steps (Phase 5)

1. Implement ARIMA model
2. Implement Prophet model
3. Implement LSTM with attention
4. Compare all models on validation set
5. Select best performing model
6. Final test set evaluation

---

**Phase 4 Status:** ✅ COMPLETE  
**Threshold Established:** 53.60%  
**Ready for Phase 5:** ✅ YES
