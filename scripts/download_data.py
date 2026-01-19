# Data Collection Script
# Downloads silver price dataset from Kaggle

import os
import subprocess

# Dataset details
DATASET = "muhammadaammartufail/silver-prices-10-year-data-and-2026-forecast"
OUTPUT_DIR = "../data/raw"

def download_dataset():
    """Download dataset using Kaggle API"""
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Download using kaggle CLI
    cmd = f"kaggle datasets download -d {DATASET} -p {OUTPUT_DIR} --unzip"
    
    print(f"Downloading {DATASET}...")
    print(f"Command: {cmd}")
    print("\nNote: Requires Kaggle API credentials (~/.kaggle/kaggle.json)")
    print("Get your API key from: https://www.kaggle.com/account")
    
    try:
        subprocess.run(cmd, shell=True, check=True)
        print("\n✅ Download complete!")
        print(f"Files saved to: {OUTPUT_DIR}/")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Download failed: {e}")
        print("\nManual download instructions:")
        print(f"1. Go to: https://www.kaggle.com/datasets/{DATASET}")
        print("2. Click 'Download' button")
        print(f"3. Extract ZIP to: {OUTPUT_DIR}/")

if __name__ == "__main__":
    download_dataset()
