# Data Inspection & Quality Assessment Script
# Phase 1: Silver Price Dataset Analysis

import pandas as pd
import numpy as np
from pathlib import Path

# File paths
DATA_RAW = Path("../data/raw")
HISTORICAL_FILE = DATA_RAW / "silver_prices_data.csv"
FORECAST_FILE = DATA_RAW / "silver_price_forecast_2026.csv"

def inspect_data():
    """Load and inspect both CSV files"""
    
    print("="*80)
    print("PHASE 1: DATA COLLECTION & QUALITY ASSESSMENT")
    print("="*80)
    
    # Load historical data
    print("\n1. HISTORICAL DATA (2016-2026)")
    print("-" * 80)
    df_hist = pd.read_csv(HISTORICAL_FILE)
    print(f"Shape: {df_hist.shape}")
    print(f"\nColumns: {list(df_hist.columns)}")
    print(f"\nFirst 5 rows:\n{df_hist.head()}")
    print(f"\nData Types:\n{df_hist.dtypes}")
    print(f"\nMissing Values:\n{df_hist.isnull().sum()}")
    print(f"\nBasic Stats:\n{df_hist.describe()}")
    
    # Load forecast data
    print("\n\n2. FORECAST DATA (Q1 2026)")
    print("-" * 80)
    df_forecast = pd.read_csv(FORECAST_FILE)
    print(f"Shape: {df_forecast.shape}")
    print(f"\nColumns: {list(df_forecast.columns)}")
    print(f"\nFirst 5 rows:\n{df_forecast.head()}")
    print(f"\nData Types:\n{df_forecast.dtypes}")
    print(f"\nMissing Values:\n{df_forecast.isnull().sum()}")
    
    # Date range
    print("\n\n3. DATE RANGE ANALYSIS")
    print("-" * 80)
    if 'Date' in df_hist.columns:
        df_hist['Date'] = pd.to_datetime(df_hist['Date'])
        print(f"Historical: {df_hist['Date'].min()} to {df_hist['Date'].max()}")
        print(f"Total Days: {len(df_hist)}")
    
    if 'Date' in df_forecast.columns:
        df_forecast['Date'] = pd.to_datetime(df_forecast['Date'])
        print(f"Forecast: {df_forecast['Date'].min()} to {df_forecast['Date'].max()}")
        print(f"Total Days: {len(df_forecast)}")
    
    # Data quality checks
    print("\n\n4. DATA QUALITY CHECKS")
    print("-" * 80)
    
    # Check for duplicates
    print(f"Duplicate rows (historical): {df_hist.duplicated().sum()}")
    print(f"Duplicate dates (historical): {df_hist['Date'].duplicated().sum() if 'Date' in df_hist.columns else 'N/A'}")
    
    # Check for missing values
    missing_pct = (df_hist.isnull().sum() / len(df_hist) * 100)
    print(f"\nMissing % (historical):\n{missing_pct[missing_pct > 0]}")
    
    # Check for outliers (using IQR method on Close price)
    if 'Close' in df_hist.columns:
        Q1 = df_hist['Close'].quantile(0.25)
        Q3 = df_hist['Close'].quantile(0.75)
        IQR = Q3 - Q1
        outliers = ((df_hist['Close'] < (Q1 - 1.5 * IQR)) | (df_hist['Close'] > (Q3 + 1.5 * IQR))).sum()
        print(f"\nOutliers (Close price, IQR method): {outliers} ({outliers/len(df_hist)*100:.2f}%)")
    
    print("\n" + "="*80)
    print("✅ Data inspection complete!")
    print("="*80)
    
    return df_hist, df_forecast

if __name__ == "__main__":
    df_historical, df_forecast = inspect_data()
