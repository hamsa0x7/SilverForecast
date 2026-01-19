# Phase 3: Feature Engineering
# Silver Price Forecasting - Create Features for ML Models

import csv
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).parent.parent.parent  # Go up from src/features to project root
RAW_DATA = BASE_DIR / "data" / "raw" / "silver_prices_data.csv"
PROCESSED_DATA = BASE_DIR / "data" / "processed" / "silver_features.csv"

def load_prices():
    """Load historical price data"""
    prices = []
    dates = []
    
    with open(RAW_DATA, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                prices.append(float(row['Close']))
                dates.append(row['Date'])
            except (ValueError, KeyError, TypeError):
                pass
    
    return dates, prices

def calculate_returns(prices):
    """Calculate daily returns"""
    returns = [0.0]  # First day has no return
    for i in range(1, len(prices)):
        ret = (prices[i] - prices[i-1]) / prices[i-1] * 100
        returns.append(ret)
    return returns

def calculate_sma(prices, window):
    """Calculate Simple Moving Average"""
    sma = []
    for i in range(len(prices)):
        if i < window - 1:
            sma.append(0.0)  # Not enough data
        else:
            avg = sum(prices[i-window+1:i+1]) / window
            sma.append(avg)
    return sma

def calculate_rsi(prices, period=14):
    """Calculate Relative Strength Index"""
    rsi = []
    
    for i in range(len(prices)):
        if i < period:
            rsi.append(50.0)  # Neutral RSI
            continue
        
        gains = []
        losses = []
        
        for j in range(i-period+1, i+1):
            change = prices[j] - prices[j-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        
        if avg_loss == 0:
            rsi.append(100.0)
        else:
            rs = avg_gain / avg_loss
            rsi_val = 100 - (100 / (1 + rs))
            rsi.append(rsi_val)
    
    return rsi

def calculate_bollinger_bands(prices, window=20):
    """Calculate Bollinger Bands distance from middle"""
    bb_distance = []
    
    for i in range(len(prices)):
        if i < window - 1:
            bb_distance.append(0.0)
            continue
        
        # Calculate moving average
        window_prices = prices[i-window+1:i+1]
        sma = sum(window_prices) / window
        
        # Calculate standard deviation
        variance = sum((p - sma) ** 2 for p in window_prices) / window
        std_dev = variance ** 0.5
        
        # Distance from middle band (in std devs)
        if std_dev == 0:
            bb_distance.append(0.0)
        else:
            distance = (prices[i] - sma) / std_dev
            bb_distance.append(distance)
    
    return bb_distance

def calculate_momentum(prices, window=5):
    """Calculate price momentum"""
    momentum = []
    
    for i in range(len(prices)):
        if i < window:
            momentum.append(0.0)
        else:
            mom = (prices[i] - prices[i-window]) / prices[i-window] * 100
            momentum.append(mom)
    
    return momentum

def calculate_volatility(prices, window=30):
    """Calculate rolling volatility"""
    volatility = []
    
    for i in range(len(prices)):
        if i < window - 1:
            volatility.append(0.0)
            continue
        
        window_prices = prices[i-window+1:i+1]
        mean = sum(window_prices) / window
        variance = sum((p - mean) ** 2 for p in window_prices) / window
        vol = variance ** 0.5
        volatility.append(vol)
    
    return volatility

def create_lag_features(prices, lags=[1, 7, 30]):
    """Create lag features"""
    lag_features = {f'lag_{lag}': [] for lag in lags}
    
    for i in range(len(prices)):
        for lag in lags:
            if i < lag:
                lag_features[f'lag_{lag}'].append(0.0)
            else:
                lag_features[f'lag_{lag}'].append(prices[i-lag])
    
    return lag_features

def create_target(prices):
    """Create directional target (1=up, 0=down)"""
    target = []
    
    for i in range(len(prices) - 1):
        direction = 1 if prices[i+1] > prices[i] else 0
        target.append(direction)
    
    target.append(-1)  # Last day has no target
    return target

def engineer_features():
    """Main feature engineering pipeline"""
    
    print("="*80)
    print("PHASE 3: FEATURE ENGINEERING")
    print("="*80)
    
    # Load data
    print("\n📊 Loading data...")
    dates, prices = load_prices()
    print(f"✅ Loaded {len(prices)} price points")
    
    # Create features
    print("\n🔧 Creating features...")
    
    print("  - Daily returns")
    returns = calculate_returns(prices)
    
    print("  - Moving averages (5, 20, 50-day)")
    sma_5 = calculate_sma(prices, 5)
    sma_20 = calculate_sma(prices, 20)
    sma_50 = calculate_sma(prices, 50)
    
    print("  - RSI (14-period)")
    rsi = calculate_rsi(prices, 14)
    
    print("  - Bollinger Bands")
    bb_dist = calculate_bollinger_bands(prices, 20)
    
    print("  - Momentum (5-day)")
    momentum = calculate_momentum(prices, 5)
    
    print("  - Volatility (30-day rolling)")
    volatility = calculate_volatility(prices, 30)
    
    print("  - Lag features (1, 7, 30 days)")
    lag_features = create_lag_features(prices, [1, 7, 30])
    
    print("  - Target variable (direction)")
    target = create_target(prices)
    
    # Save processed data
    print("\n💾 Saving processed features...")
    PROCESSED_DATA.parent.mkdir(parents=True, exist_ok=True)
    
    with open(PROCESSED_DATA, 'w', newline='') as f:
        fieldnames = ['date', 'price', 'return', 'sma_5', 'sma_20', 'sma_50', 
                     'rsi', 'bb_distance', 'momentum', 'volatility',
                     'lag_1', 'lag_7', 'lag_30', 'target']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for i in range(len(prices)):
            writer.writerow({
                'date': dates[i],
                'price': prices[i],
                'return': returns[i],
                'sma_5': sma_5[i],
                'sma_20': sma_20[i],
                'sma_50': sma_50[i],
                'rsi': rsi[i],
                'bb_distance': bb_dist[i],
                'momentum': momentum[i],
                'volatility': volatility[i],
                'lag_1': lag_features['lag_1'][i],
                'lag_7': lag_features['lag_7'][i],
                'lag_30': lag_features['lag_30'][i],
                'target': target[i]
            })
    
    print(f"✅ Saved to: {PROCESSED_DATA}")
    
    # Summary
    print("\n📊 FEATURE SUMMARY")
    print("-" * 80)
    print(f"Total features created: 13")
    print(f"  - Price-based: 1 (close price)")
    print(f"  - Derived: 2 (returns, momentum)")
    print(f"  - Technical indicators: 4 (SMA-5, 20, 50, RSI)")
    print(f"  - Volatility: 2 (Bollinger, rolling vol)")
    print(f"  - Lag features: 3 (1, 7, 30 days)")
    print(f"  - Target: 1 (direction: 1=up, 0=down)")
    
    # Check target distribution
    up_days = sum(1 for t in target if t == 1)
    down_days = sum(1 for t in target if t == 0)
    total_valid = up_days + down_days
    
    print(f"\n📈 TARGET DISTRIBUTION")
    print("-" * 80)
    print(f"Up days (1): {up_days} ({up_days/total_valid*100:.1f}%)")
    print(f"Down days (0): {down_days} ({down_days/total_valid*100:.1f}%)")
    print(f"Class balance: {'✅ Good' if abs(up_days - down_days) < total_valid * 0.1 else '⚠️ Imbalanced'}")
    
    print("\n" + "="*80)
    print("✅ Feature Engineering Complete!")
    print("="*80)
    print(f"\n📝 Next: Phase 4 - Train baseline model")

if __name__ == "__main__":
    engineer_features()
