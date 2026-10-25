"""
Automated Data Quality & Schema Integrity Tests for Processed Datasets
Validates that cleaning pipelines produced deterministic, anomaly-free datasets.
"""
import pytest
import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

@pytest.fixture(scope="module")
def superstore_df():
    path = PROCESSED_DIR / "superstore_cleaned.csv"
    assert path.exists(), "Processed superstore dataset missing"
    return pd.read_csv(path, dtype={'Postal Code': str})

@pytest.fixture(scope="module")
def telco_df():
    path = PROCESSED_DIR / "telco_churn_cleaned.csv"
    assert path.exists(), "Processed telco churn dataset missing"
    return pd.read_csv(path)

@pytest.fixture(scope="module")
def financial_df():
    path = PROCESSED_DIR / "financial_sample_cleaned.csv"
    assert path.exists(), "Processed financial dataset missing"
    return pd.read_csv(path)

# --- Superstore Quality Tests ---
def test_superstore_dimensions_and_nulls(superstore_df):
    assert len(superstore_df) == 9994
    # Zero nulls across critical operational columns
    critical_cols = ['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Customer ID',
                     'Postal Code', 'Sales', 'Quantity', 'Discount', 'Profit']
    null_counts = superstore_df[critical_cols].isnull().sum()
    assert (null_counts == 0).all(), f"Found nulls in critical columns: {null_counts[null_counts > 0]}"

def test_superstore_burlington_postal_code(superstore_df):
    # Verify Burlington VT postal code imputation
    burlington = superstore_df[superstore_df['State'] == 'Vermont']
    assert (burlington['Postal Code'] == '05401').all()

def test_superstore_numeric_boundaries(superstore_df):
    assert (superstore_df['Sales'] > 0).all()
    assert (superstore_df['Quantity'] >= 1).all()
    assert (superstore_df['Discount'] >= 0.0).all()
    assert (superstore_df['Discount'] <= 1.0).all()
    assert (superstore_df['Shipping Days'] >= 0).all()

# --- Telco Churn Quality Tests ---
def test_telco_dimensions_and_charges(telco_df):
    assert len(telco_df) == 7043
    assert telco_df['TotalCharges'].isnull().sum() == 0
    # Verify zero-tenure rows have 0.0 total charges
    zero_tenure = telco_df[telco_df['tenure'] == 0]
    assert len(zero_tenure) == 11
    assert (zero_tenure['TotalCharges'] == 0.0).all()

def test_telco_cohorts_and_churn_flag(telco_df):
    assert telco_df['Tenure Cohort'].isnull().sum() == 0
    assert set(telco_df['Churn_Numeric'].unique()) == {0, 1}
    assert (telco_df['MonthlyCharges'] > 0).all()

# --- Financial Sample Quality Tests ---
def test_financial_dimensions_and_cleaning(financial_df):
    assert len(financial_df) == 700
    assert 'Sales' in financial_df.columns
    assert ' Sales' not in financial_df.columns
    assert financial_df['Discount Band'].isnull().sum() == 0
    assert (financial_df['Units Sold'] > 0).all()

def test_financial_accounting_identity(financial_df):
    # Gross Sales - Discounts = Sales within 5-cent rounding tolerance from original Excel
    diff = (financial_df['Gross Sales'] - financial_df['Discounts']) - financial_df['Sales']
    assert np.allclose(diff, 0.0, atol=0.05), "Accounting identity Gross - Discounts = Sales violated"
