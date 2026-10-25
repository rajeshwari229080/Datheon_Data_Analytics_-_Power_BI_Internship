"""
Deterministic Data Cleaning & Transformation Pipeline
Cleans and standardizes raw datasets for Superstore, Telco Churn, and Financial Sample,
resolving discovered anomalies and outputting validated processed datasets.
"""
import sys
from pathlib import Path
from typing import Tuple, Dict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import pandas as pd
import numpy as np

from src.data_loader import (
    load_raw_superstore,
    load_raw_telco,
    load_raw_financial,
    DATA_PROCESSED_DIR,
    ensure_directories
)

def clean_superstore() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Clean raw Superstore data, extracting three distinct tables:
    1. Cleaned Orders (9,994 transaction rows)
    2. Regional Managers (People lookup)
    3. Order Returns
    """
    ensure_directories()
    raw_df = load_raw_superstore()
    
    # 1. Separate Orders (Rows 0 to 9993)
    orders_df = raw_df.iloc[:9994].copy()
    
    # Standardize column names (strip whitespace)
    orders_df.columns = [c.strip() for c in orders_df.columns]
    
    # Type conversions
    orders_df['Row ID'] = orders_df['Row ID'].astype(int)
    orders_df['Order Date'] = pd.to_datetime(orders_df['Order Date'], format='%m/%d/%Y', errors='coerce')
    orders_df['Ship Date'] = pd.to_datetime(orders_df['Ship Date'], format='%m/%d/%Y', errors='coerce')
    
    # Impute missing Postal Code for Burlington, Vermont (ZIP 05401)
    orders_df['Postal Code'] = orders_df['Postal Code'].fillna(5401)
    orders_df['Postal Code'] = orders_df['Postal Code'].astype(int).astype(str).str.zfill(5)
    
    # Numeric types
    orders_df['Sales'] = orders_df['Sales'].astype(float).round(4)
    orders_df['Quantity'] = orders_df['Quantity'].astype(int)
    orders_df['Discount'] = orders_df['Discount'].astype(float).round(4)
    orders_df['Profit'] = orders_df['Profit'].astype(float).round(4)
    
    # Temporal feature engineering
    orders_df['Order Year'] = orders_df['Order Date'].dt.year
    orders_df['Order Month'] = orders_df['Order Date'].dt.month
    orders_df['Order Month Name'] = orders_df['Order Date'].dt.month_name()
    orders_df['Order YearMonth'] = orders_df['Order Date'].dt.to_period('M').astype(str)
    orders_df['Order DayOfWeek'] = orders_df['Order Date'].dt.day_name()
    orders_df['Shipping Days'] = (orders_df['Ship Date'] - orders_df['Order Date']).dt.days
    
    # Financial & Commercial metrics
    orders_df['Profit Margin'] = np.where(orders_df['Sales'] > 0, orders_df['Profit'] / orders_df['Sales'], 0.0)
    
    # Discount bands for elasticity analysis
    discount_bins = [-0.01, 0.001, 0.10, 0.20, 0.50, 1.00]
    discount_labels = ['0% (None)', '1% - 10%', '11% - 20%', '21% - 50%', '> 50% (Extreme)']
    orders_df['Discount Band'] = pd.cut(orders_df['Discount'], bins=discount_bins, labels=discount_labels)
    
    # 2. Extract Regional People (Rows 9995 to 9998)
    people_slice = raw_df.iloc[9995:9999, :2].copy()
    people_slice.columns = ['Regional Manager', 'Region']
    people_df = people_slice.dropna().drop_duplicates().reset_index(drop=True)
    
    # 3. Extract Order Returns (Rows 10000 to 10799)
    returns_slice = raw_df.iloc[10000:10800, :2].copy()
    returns_slice.columns = ['Returned', 'Order ID']
    returns_df = returns_slice.dropna().drop_duplicates().reset_index(drop=True)
    
    # Merge return flag into orders for analytical convenience
    returned_order_ids = set(returns_df['Order ID'])
    orders_df['Is Returned'] = orders_df['Order ID'].isin(returned_order_ids)
    
    # Save artifacts
    orders_df.to_csv(DATA_PROCESSED_DIR / "superstore_cleaned.csv", index=False)
    people_df.to_csv(DATA_PROCESSED_DIR / "superstore_people.csv", index=False)
    returns_df.to_csv(DATA_PROCESSED_DIR / "superstore_returns.csv", index=False)
    
    return orders_df, people_df, returns_df

def clean_telco() -> pd.DataFrame:
    """
    Clean IBM Telco Customer Churn data:
    - Safely convert TotalCharges, handling 11 blank spaces with 0.0 where tenure == 0
    - Define tenure cohorts (0-12, 13-24, 25-36, 37-48, 49-60, 61-72 months)
    - Add binary Churn_Numeric
    """
    ensure_directories()
    df = load_raw_telco()
    df.columns = [c.strip() for c in df.columns]
    
    # Clean TotalCharges
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'].astype(str).str.strip(), errors='coerce')
    df['TotalCharges'] = df['TotalCharges'].fillna(0.0).round(2)
    
    # Numeric types
    df['tenure'] = df['tenure'].astype(int)
    df['MonthlyCharges'] = df['MonthlyCharges'].astype(float).round(2)
    
    # Churn numeric binary flag
    df['Churn_Numeric'] = (df['Churn'].str.strip() == 'Yes').astype(int)
    
    # Tenure Cohorts
    cohort_bins = [-1, 12, 24, 36, 48, 60, 72]
    cohort_labels = ['0-12 Months', '13-24 Months', '25-36 Months', '37-48 Months', '49-60 Months', '61-72 Months']
    df['Tenure Cohort'] = pd.cut(df['tenure'], bins=cohort_bins, labels=cohort_labels)
    
    # Save processed artifact
    dest = DATA_PROCESSED_DIR / "telco_churn_cleaned.csv"
    df.to_csv(dest, index=False)
    return df

def clean_financial() -> pd.DataFrame:
    """
    Clean Microsoft Financial Sample data:
    - Strip whitespace from headers (' Sales' -> 'Sales')
    - Fill null Discount Band with 'None'
    - Cast types and derive financial ratios
    """
    ensure_directories()
    df = load_raw_financial()
    df.columns = [c.strip() for c in df.columns]
    
    # Fill Discount Band with 'No Discount' (avoiding literal 'None' which pandas parses as NaN)
    df['Discount Band'] = df['Discount Band'].fillna('No Discount').replace({'None': 'No Discount'})
    
    # Type casts
    float_cols = ['Units Sold', 'Manufacturing Price', 'Sale Price', 'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit']
    for c in float_cols:
        df[c] = df[c].astype(float).round(2)
        
    df['Date'] = pd.to_datetime(df['Date'])
    df['Year'] = df['Year'].astype(int)
    df['Month Number'] = df['Month Number'].astype(int)
    df['Month Name'] = df['Month Name'].str.strip()
    df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
    
    # Managerial accounting metrics
    df['Gross Profit Margin'] = np.where(df['Sales'] > 0, (df['Profit'] / df['Sales']).round(4), 0.0)
    df['COGS Ratio'] = np.where(df['Sales'] > 0, (df['COGS'] / df['Sales']).round(4), 0.0)
    df['Discount Impact %'] = np.where(df['Gross Sales'] > 0, (df['Discounts'] / df['Gross Sales']).round(4), 0.0)
    
    # Save processed artifact
    dest = DATA_PROCESSED_DIR / "financial_sample_cleaned.csv"
    df.to_csv(dest, index=False)
    return df

def run_all_cleaning():
    """Run complete deterministic cleaning pipeline."""
    print("Executing Superstore cleaning...")
    orders_df, people_df, returns_df = clean_superstore()
    print(f"-> Orders: {orders_df.shape}, People: {people_df.shape}, Returns: {returns_df.shape}")
    
    print("Executing Telco Churn cleaning...")
    telco_df = clean_telco()
    print(f"-> Telco: {telco_df.shape}")
    
    print("Executing Financial Sample cleaning...")
    fin_df = clean_financial()
    print(f"-> Financial: {fin_df.shape}")
    print("All datasets cleaned and stored in data/processed/ successfully.")

if __name__ == "__main__":
    run_all_cleaning()
