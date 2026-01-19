# Phase 2: Exploratory Data Analysis (EDA)
# Silver Price Forecasting - Time Series Analysis

import csv
from datetime import datetime
from collections import Counter

from pathlib import Path

# File paths
BASE_DIR = Path(__file__).parent.parent
DATA_FILE = BASE_DIR / "data" / "raw" / "silver_prices_data.csv"

def load_csv_basic(filename):
    """Load CSV without pandas (basic Python only)"""
    data = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

def analyze_data():
    """Perform basic EDA on silver price data"""
    
    print("="*80)
    print("PHASE 2: EXPLORATORY DATA ANALYSIS")
    print("="*80)
    
    # Load data
    print("\n📊 Loading data...")
    data = load_csv_basic(DATA_FILE)
    print(f"✅ Loaded {len(data)} records")
    
    # Extract prices
    prices = []
    dates = []
    volumes = []
    
    for row in data:
        try:
            prices.append(float(row['Close']))
            dates.append(row['Date'])
            # Handle missing volume data
            try:
                vol = float(row['Volume']) if row['Volume'] and row['Volume'] != '' else 0
                volumes.append(vol)
            except (ValueError, TypeError):
                volumes.append(0)
        except (ValueError, KeyError, TypeError):
            pass
    
    print(f"\n1. BASIC STATISTICS")
    print("-" * 80)
    print(f"Total data points: {len(prices)}")
    print(f"Date range: {dates[0]} to {dates[-1]}")
    print(f"\nPrice Statistics:")
    print(f"  Min: ${min(prices):.2f}")
    print(f"  Max: ${max(prices):.2f}")
    print(f"  Mean: ${sum(prices)/len(prices):.2f}")
    print(f"  Range: ${max(prices) - min(prices):.2f}")
    
    # Calculate median
    sorted_prices = sorted(prices)
    median = sorted_prices[len(sorted_prices)//2]
    print(f"  Median: ${median:.2f}")
    
    # Calculate standard deviation
    mean = sum(prices) / len(prices)
    variance = sum((x - mean) ** 2 for x in prices) / len(prices)
    std_dev = variance ** 0.5
    print(f"  Std Dev: ${std_dev:.2f}")
    
    print(f"\n2. TREND ANALYSIS")
    print("-" * 80)
    
    # Calculate daily returns
    returns = []
    for i in range(1, len(prices)):
        daily_return = (prices[i] - prices[i-1]) / prices[i-1] * 100
        returns.append(daily_return)
    
    positive_days = sum(1 for r in returns if r > 0)
    negative_days = sum(1 for r in returns if r < 0)
    
    print(f"Daily Returns:")
    print(f"  Positive days: {positive_days} ({positive_days/len(returns)*100:.1f}%)")
    print(f"  Negative days: {negative_days} ({negative_days/len(returns)*100:.1f}%)")
    print(f"  Mean daily return: {sum(returns)/len(returns):.3f}%")
    
    # Detect overall trend
    first_100 = sum(prices[:100]) / 100
    last_100 = sum(prices[-100:]) / 100
    trend_change = ((last_100 - first_100) / first_100) * 100
    
    print(f"\nOverall Trend (first 100 vs last 100 days):")
    print(f"  First 100 days avg: ${first_100:.2f}")
    print(f"  Last 100 days avg: ${last_100:.2f}")
    print(f"  Change: {trend_change:+.2f}%")
    
    print(f"\n3. OUTLIER DETECTION (IQR Method)")
    print("-" * 80)
    
    # IQR method
    Q1_idx = len(sorted_prices) // 4
    Q3_idx = 3 * len(sorted_prices) // 4
    Q1 = sorted_prices[Q1_idx]
    Q3 = sorted_prices[Q3_idx]
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = [p for p in prices if p < lower_bound or p > upper_bound]
    print(f"Q1 (25th percentile): ${Q1:.2f}")
    print(f"Q3 (75th percentile): ${Q3:.2f}")
    print(f"IQR: ${IQR:.2f}")
    print(f"Lower bound: ${lower_bound:.2f}")
    print(f"Upper bound: ${upper_bound:.2f}")
    print(f"Outliers detected: {len(outliers)} ({len(outliers)/len(prices)*100:.2f}%)")
    
    if outliers:
        print(f"\nOutlier price range: ${min(outliers):.2f} - ${max(outliers):.2f}")
    
    print(f"\n4. VOLATILITY ANALYSIS")
    print("-" * 80)
    
    # Calculate daily price changes
    changes = [abs(prices[i] - prices[i-1]) for i in range(1, len(prices))]
    avg_change = sum(changes) / len(changes)
    max_change = max(changes)
    
    print(f"Average daily price change: ${avg_change:.2f}")
    print(f"Maximum daily price change: ${max_change:.2f}")
    print(f"Volatility (std of returns): {(sum((r - sum(returns)/len(returns))**2 for r in returns) / len(returns))**0.5:.3f}%")
    
    print(f"\n5. DIRECTIONAL ACCURACY BASELINE")
    print("-" * 80)
    
    # Calculate naive forecast accuracy (tomorrow = today)
    correct_predictions = 0
    for i in range(1, len(prices)-1):
        actual_direction = 1 if prices[i+1] > prices[i] else 0
        predicted_direction = 1 if prices[i] > prices[i-1] else 0
        if actual_direction == predicted_direction:
            correct_predictions += 1
    
    baseline_accuracy = correct_predictions / (len(prices) - 2) * 100
    print(f"Naive Forecast (persistence model):")
    print(f"  Directional Accuracy: {baseline_accuracy:.2f}%")
    print(f"  Beat random (50%)?: {'✅ YES' if baseline_accuracy > 50 else '❌ NO'}")
    
    print("\n" + "="*80)
    print("✅ EDA Complete!")
    print("="*80)
    
    print(f"\n📝 KEY FINDINGS:")
    print(f"1. Price range: ${min(prices):.2f} - ${max(prices):.2f}")
    print(f"2. Overall trend: {'+' if trend_change > 0 else ''}{trend_change:.1f}% over 10 years")
    print(f"3. Volatility: {std_dev:.2f} std dev")
    print(f"4. Baseline model accuracy: {baseline_accuracy:.1f}% (our goal: >60%)")
    print(f"5. Outliers: {len(outliers)} days with unusual prices")

if __name__ == "__main__":
    analyze_data()
