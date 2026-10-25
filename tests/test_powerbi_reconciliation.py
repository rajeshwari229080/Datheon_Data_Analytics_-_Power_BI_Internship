"""
Reconciliation Tests: Star Schema Model vs. Cleaned Superstore Transactions
Asserts zero variance between star schema aggregations and the flat cleaned dataset.
"""
import pytest
import pandas as pd
import numpy as np
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
STAR_DIR = PROCESSED_DIR / "star_schema"

@pytest.fixture(scope="module")
def flat_orders():
    return pd.read_csv(PROCESSED_DIR / "superstore_cleaned.csv", dtype={'Postal Code': str})

@pytest.fixture(scope="module")
def star_fact():
    return pd.read_csv(STAR_DIR / "FactSales.csv", dtype={'Postal Code': str})

@pytest.fixture(scope="module")
def star_dims():
    return {
        "date": pd.read_csv(STAR_DIR / "DimDate.csv"),
        "customer": pd.read_csv(STAR_DIR / "DimCustomer.csv"),
        "product": pd.read_csv(STAR_DIR / "DimProduct.csv"),
        "geography": pd.read_csv(STAR_DIR / "DimGeography.csv", dtype={'Postal Code': str})
    }

def test_fact_sales_totals_reconciliation(flat_orders, star_fact):
    assert len(flat_orders) == len(star_fact)
    assert np.isclose(flat_orders['Sales'].sum(), star_fact['Sales'].sum(), atol=1e-4)
    assert np.isclose(flat_orders['Profit'].sum(), star_fact['Profit'].sum(), atol=1e-4)
    assert flat_orders['Quantity'].sum() == star_fact['Quantity'].sum()
    assert flat_orders['Order ID'].nunique() == star_fact['Order ID'].nunique()

def test_star_dimensional_joins_reconciliation(star_fact, star_dims):
    # Perform inner joins across all dimensions
    joined = (
        star_fact
        .merge(star_dims['date'], left_on='OrderDateKey', right_on='DateKey', how='inner')
        .merge(star_dims['customer'], on='Customer ID', how='inner')
        .merge(star_dims['product'], on='Product ID', how='inner')
        .merge(star_dims['geography'], on='Postal Code', how='inner')
    )
                      
    assert len(joined) == len(star_fact), "Orphan records detected during dimensional joins"
    assert np.isclose(joined['Sales'].sum(), star_fact['Sales'].sum(), atol=1e-4)
    assert np.isclose(joined['Profit'].sum(), star_fact['Profit'].sum(), atol=1e-4)

def test_category_margin_reconciliation(flat_orders, star_fact, star_dims):
    flat_cat = flat_orders.groupby('Category')['Sales'].sum().sort_index()
    
    joined = star_fact.merge(star_dims['product'], on='Product ID', how='inner')
    star_cat = joined.groupby('Category')['Sales'].sum().sort_index()
    
    assert np.allclose(flat_cat.values, star_cat.values, atol=1e-4)
