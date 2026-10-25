"""
Data Ingestion and Loading Module
Handles verified downloading, local caching, and raw data ingestion
for Superstore Sales, IBM Telco Churn, and Financial Sample datasets.
"""
import os
import urllib.request
from pathlib import Path
from typing import Dict, Optional
import pandas as pd
import openpyxl

# Project Root Directory Resolution
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_RAW_DIR = PROJECT_ROOT / "data" / "raw"
DATA_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

DATASET_URLS = {
    "superstore_sales.csv": "https://www.datheon.in/datasets/superstore_sales.csv",
    "telco_customer_churn.csv": "https://www.datheon.in/datasets/telco_customer_churn.csv",
    "financial_sample.xlsx": "https://www.datheon.in/datasets/financial_sample.xlsx",
}

def ensure_directories():
    """Ensure raw and processed data directories exist."""
    DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)
    DATA_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

def download_dataset(filename: str, force: bool = False) -> Path:
    """
    Download a dataset from the official Datheon repository if not already cached.
    
    Args:
        filename: Name of the dataset file.
        force: If True, re-download even if already present.
        
    Returns:
        Path to the downloaded local file.
    """
    ensure_directories()
    dest = DATA_RAW_DIR / filename
    
    if dest.exists() and not force:
        return dest
        
    if filename not in DATASET_URLS:
        raise ValueError(f"Unknown dataset filename: {filename}. Available: {list(DATASET_URLS.keys())}")
        
    url = DATASET_URLS[filename]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) RISK-Suite/1.0"}
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req, timeout=45) as response, open(dest, "wb") as out_file:
        out_file.write(response.read())
        
    return dest

def load_raw_superstore(force_download: bool = False) -> pd.DataFrame:
    """
    Load raw Superstore retail sales dataset.
    Note: Source CSV contains appended tables (Regional Managers and Returns)
    starting at row 9994 which are handled during data cleaning.
    """
    filepath = download_dataset("superstore_sales.csv", force=force_download)
    return pd.read_csv(filepath, encoding="latin1")

def load_raw_telco(force_download: bool = False) -> pd.DataFrame:
    """Load raw IBM Telco Customer Churn dataset."""
    filepath = download_dataset("telco_customer_churn.csv", force=force_download)
    return pd.read_csv(filepath)

def load_raw_financial(force_download: bool = False) -> pd.DataFrame:
    """Load raw Microsoft Financial Sample Excel dataset."""
    filepath = download_dataset("financial_sample.xlsx", force=force_download)
    return pd.read_excel(filepath)

if __name__ == "__main__":
    ensure_directories()
    print("Verifying datasets ingestion...")
    df_s = load_raw_superstore()
    print(f"Superstore loaded: {df_s.shape[0]} rows, {df_s.shape[1]} cols")
    df_t = load_raw_telco()
    print(f"Telco loaded: {df_t.shape[0]} rows, {df_t.shape[1]} cols")
    df_f = load_raw_financial()
    print(f"Financial sample loaded: {df_f.shape[0]} rows, {df_f.shape[1]} cols")
    print("Ingestion verification complete.")
