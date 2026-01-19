# Phase 4: Baseline Model & Data Split
# Silver Price Forecasting - Establish Performance Threshold

import csv
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).parent.parent.parent
FEATURES_FILE = BASE_DIR / "data" / "processed" / "silver_features.csv"

def load_features():
    """Load processed features"""
    data = []
    with open(FEATURES_FILE, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def split_data(data, train_pct=0.70, val_pct=0.15):
    """Time series split (no shuffling!)"""
    n = len(data)
    
    train_end = int(n * train_pct)
    val_end = int(n * (train_pct + val_pct))
    
    train = data[:train_end]
    val = data[train_end:val_end]
    test = data[val_end:]
    
    return train, val, test

def baseline_naive_persistence(data):
    """Naive forecast: tomorrow = today"""
    correct = 0
    total = 0
    
    for i in range(1, len(data)):
        try:
            current_target = int(float(data[i]['target']))
            previous_target = int(float(data[i-1]['target']))
            
            # Skip if target is -1 (last day)
            if current_target == -1 or previous_target == -1:
                continue
            
            # Prediction: tomorrow will be same direction as today
            prediction = previous_target
            actual = current_target
            
            if prediction == actual:
                correct += 1
            total += 1
        except (ValueError, KeyError):
            continue
    
    accuracy = (correct / total * 100) if total > 0 else 0
    return accuracy, correct, total

def baseline_moving_average_crossover(data):
    """MA Crossover: if SMA5 > SMA20, predict up"""
    correct = 0
    total = 0
    
    for i in range(len(data)):
        try:
            target = int(float(data[i]['target']))
            sma_5 = float(data[i]['sma_5'])
            sma_20 = float(data[i]['sma_20'])
            
            # Skip if target is -1 or SMAs not calculated yet
            if target == -1 or sma_5 == 0 or sma_20 == 0:
                continue
            
            # Prediction: up if SMA5 > SMA20
            prediction = 1 if sma_5 > sma_20 else 0
            
            if prediction == target:
                correct += 1
            total += 1
        except (ValueError, KeyError):
            continue
    
    accuracy = (correct / total * 100) if total > 0 else 0
    return accuracy, correct, total

def analyze_baselines():
    """Main baseline analysis"""
    
    print("="*80)
    print("PHASE 4: BASELINE MODEL & DATA SPLIT")
    print("="*80)
    
    # Load data
    print("\n📊 Loading processed features...")
    data = load_features()
    print(f"✅ Loaded {len(data)} samples")
    
    # Split data
    print("\n✂️ Splitting data (time series split - no shuffling)...")
    train, val, test = split_data(data, train_pct=0.70, val_pct=0.15)
    
    print(f"  Train set: {len(train)} samples (~70%)")
    print(f"  Validation set: {len(val)} samples (~15%)")
    print(f"  Test set: {len(test)} samples (~15%)")
    
    # Get date ranges
    if train and val and test:
        print(f"\n📅 DATE RANGES:")
        print(f"  Train: {train[0]['date']} to {train[-1]['date']}")
        print(f"  Val: {val[0]['date']} to {val[-1]['date']}")
        print(f"  Test: {test[0]['date']} to {test[-1]['date']}")
    
    # Baseline 1: Naive Persistence
    print(f"\n📈 BASELINE 1: Naive Persistence (Tomorrow = Today)")
    print("-" * 80)
    
    train_acc, train_correct, train_total = baseline_naive_persistence(train)
    val_acc, val_correct, val_total = baseline_naive_persistence(val)
    test_acc, test_correct, test_total = baseline_naive_persistence(test)
    
    print(f"Train: {train_acc:.2f}% ({train_correct}/{train_total})")
    print(f"Val:   {val_acc:.2f}% ({val_correct}/{val_total})")
    print(f"Test:  {test_acc:.2f}% ({test_correct}/{test_total})")
    
    # Baseline 2: Moving Average Crossover
    print(f"\n📈 BASELINE 2: Moving Average Crossover (SMA5 vs SMA20)")
    print("-" * 80)
    
    train_acc2, train_correct2, train_total2 = baseline_moving_average_crossover(train)
    val_acc2, val_correct2, val_total2 = baseline_moving_average_crossover(val)
    test_acc2, test_correct2, test_total2 = baseline_moving_average_crossover(test)
    
    print(f"Train: {train_acc2:.2f}% ({train_correct2}/{train_total2})")
    print(f"Val:   {val_acc2:.2f}% ({val_correct2}/{val_total2})")
    print(f"Test:  {test_acc2:.2f}% ({test_correct2}/{test_total2})")
    
    # Summary
    print("\n" + "="*80)
    print("📊 BASELINE SUMMARY")
    print("="*80)
    
    best_baseline = max(test_acc, test_acc2)
    print(f"\nBest Baseline (Test Set): {best_baseline:.2f}%")
    print(f"Random Chance: 50.00%")
    print(f"Our Target: >60.00%")
    print(f"\n✅ Threshold to beat: {best_baseline:.2f}%")
    
    # Gap analysis
    gap_to_target = 60.0 - best_baseline
    print(f"📈 Gap to target: {gap_to_target:.2f} percentage points")
    
    if gap_to_target > 0:
        print(f"💪 Challenge: Need to improve {gap_to_target:.2f}% to hit target")
    else:
        print(f"🎯 Baseline already beats target! (Unexpected)")
    
    print("\n" + "="*80)
    print("✅ Phase 4 Complete!")
    print("="*80)
    print(f"\n📝 Next: Phase 5 - Train ML models (ARIMA, Prophet, LSTM)")
    print(f"🎯 Goal: Beat {best_baseline:.2f}% and reach >60%")

if __name__ == "__main__":
    analyze_baselines()
