"""
Data Validation and Quality Auditing Module
Implements structural schema validation, null profiling, duplicate checks,
and integrity assertions for Superstore, Telco Churn, and Financial Sample datasets.
"""
from typing import Dict, Any, List, Tuple
import pandas as pd
import numpy as np

EXPECTED_SUPERSTORE_COLUMNS = [
    'Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',
    'Customer ID', 'Customer Name', 'Segment', 'Country', 'City',
    'State', 'Postal Code', 'Region', 'Product ID', 'Category',
    'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'
]

EXPECTED_TELCO_COLUMNS = [
    'customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
    'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
    'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
    'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'
]

EXPECTED_FINANCIAL_COLUMNS = [
    'Segment', 'Country', 'Product', 'Discount Band', 'Units Sold',
    'Manufacturing Price', 'Sale Price', 'Gross Sales', 'Discounts',
    ' Sales', 'COGS', 'Profit', 'Date', 'Month Number', 'Month Name', 'Year'
]

def audit_dataset_structure(df: pd.DataFrame, expected_cols: List[str], name: str) -> Dict[str, Any]:
    """Perform structural quality audit on a pandas DataFrame."""
    total_rows = len(df)
    total_cols = len(df.columns)
    missing_cols = [c for c in expected_cols if c not in df.columns]
    unexpected_cols = [c for c in df.columns if c not in expected_cols]
    null_counts = df.isnull().sum().to_dict()
    duplicate_rows = int(df.duplicated().sum())
    
    return {
        "dataset_name": name,
        "total_rows": total_rows,
        "total_cols": total_cols,
        "schema_valid": len(missing_cols) == 0,
        "missing_columns": missing_cols,
        "unexpected_columns": unexpected_cols,
        "null_counts": null_counts,
        "duplicate_rows": duplicate_rows
    }

def audit_superstore_anomalies(df: pd.DataFrame) -> Dict[str, Any]:
    """Audit Superstore-specific anomalies including appended tables and Burlington postal codes."""
    # Check for appended metadata sheets
    appended_mask = df['Order Date'].isnull()
    appended_count = int(appended_mask.sum())
    
    # Check valid order rows (0 to 9993)
    orders_slice = df.iloc[:9994]
    burlington_null_zips = int(orders_slice[orders_slice['State'] == 'Vermont']['Postal Code'].isnull().sum())
    
    return {
        "raw_total_rows": len(df),
        "appended_table_rows": appended_count,
        "orders_row_count": len(orders_slice),
        "burlington_missing_postal_codes": burlington_null_zips,
        "exact_duplicates_in_orders": int(orders_slice.duplicated().sum())
    }

def audit_telco_anomalies(df: pd.DataFrame) -> Dict[str, Any]:
    """Audit Telco Churn specific data quality anomalies."""
    # Blank TotalCharges
    blank_total_charges = int((df['TotalCharges'].astype(str).str.strip() == '').sum())
    # Zero tenure
    zero_tenure_count = int((df['tenure'] == 0).sum())
    # Unique customer ID
    unique_customers = int(df['customerID'].nunique())
    
    return {
        "total_records": len(df),
        "blank_total_charges": blank_total_charges,
        "zero_tenure_records": zero_tenure_count,
        "unique_customer_ids": unique_customers,
        "id_uniqueness_ratio": unique_customers / len(df) if len(df) > 0 else 0
    }

def audit_financial_anomalies(df: pd.DataFrame) -> Dict[str, Any]:
    """Audit Financial Sample specific quality anomalies."""
    has_leading_space_sales = ' Sales' in df.columns
    null_discount_bands = int(df['Discount Band'].isnull().sum())
    
    return {
        "total_records": len(df),
        "has_leading_space_sales_col": has_leading_space_sales,
        "null_discount_band_count": null_discount_bands,
        "unique_products": int(df['Product'].nunique()),
        "unique_countries": int(df['Country'].nunique())
    }
