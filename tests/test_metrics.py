"""
Mathematical Invariance & Reconciliation Tests for Centralized Metrics Engine
Assures that aggregations, accounting identities, and population reconciliations hold true.
"""
import pytest
import pandas as pd
import numpy as np
from pathlib import Path

from src.metrics import (
    calculate_superstore_kpis,
    aggregate_superstore_by_dimension,
    aggregate_superstore_monthly,
    analyze_discount_elasticity,
    calculate_telco_churn_kpis,
    calculate_tenure_cohort_metrics,
    calculate_segment_churn,
    calculate_financial_kpis,
    aggregate_financial_by_dimension,
    simulate_financial_scenario
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

@pytest.fixture(scope="module")
def superstore_df():
    return pd.read_csv(PROCESSED_DIR / "superstore_cleaned.csv")

@pytest.fixture(scope="module")
def telco_df():
    return pd.read_csv(PROCESSED_DIR / "telco_churn_cleaned.csv")

@pytest.fixture(scope="module")
def financial_df():
    return pd.read_csv(PROCESSED_DIR / "financial_sample_cleaned.csv")

# --- Superstore Reconciliation Tests ---
def test_superstore_reconciliation(superstore_df):
    kpis = calculate_superstore_kpis(superstore_df)
    
    # 1. Category aggregation reconciliation
    cat_agg = aggregate_superstore_by_dimension(superstore_df, 'Category')
    assert np.isclose(cat_agg['Sales'].sum(), kpis['total_sales'], atol=0.05)
    assert np.isclose(cat_agg['Profit'].sum(), kpis['total_profit'], atol=0.05)
    assert cat_agg['Quantity'].sum() == kpis['total_quantity']
    
    # 2. Monthly aggregation reconciliation
    monthly_agg = aggregate_superstore_monthly(superstore_df)
    assert np.isclose(monthly_agg['Sales'].sum(), kpis['total_sales'], atol=0.05)
    assert np.isclose(monthly_agg['Profit'].sum(), kpis['total_profit'], atol=0.05)
    assert monthly_agg['Quantity'].sum() == kpis['total_quantity']
    
    # 3. Discount elasticity order lines count
    discount_agg = analyze_discount_elasticity(superstore_df)
    assert discount_agg['Order_Lines'].sum() == len(superstore_df)

# --- Telco Churn Reconciliation Tests ---
def test_telco_reconciliation(telco_df):
    kpis = calculate_telco_churn_kpis(telco_df)
    assert kpis['churned_customers'] + kpis['retained_customers'] == kpis['total_customers']
    assert np.isclose(kpis['churn_rate_pct'] + kpis['retention_rate_pct'], 100.0, atol=0.01)
    
    # Cohort breakdown reconciliation
    cohort = calculate_tenure_cohort_metrics(telco_df)
    assert cohort['Total_Customers'].sum() == kpis['total_customers']
    assert cohort['Churned_Customers'].sum() == kpis['churned_customers']
    assert cohort['Retained_Customers'].sum() == kpis['retained_customers']

# --- Financial Sample Reconciliation Tests ---
def test_financial_reconciliation(financial_df):
    kpis = calculate_financial_kpis(financial_df)
    
    # Reconciliation: Net Sales = Gross Sales - Discounts
    assert np.isclose(kpis['gross_sales'] - kpis['total_discounts'], kpis['net_sales'], atol=0.05)
    # Reconciliation: Profit = Net Sales - COGS
    assert np.isclose(kpis['net_sales'] - kpis['total_cogs'], kpis['total_profit'], atol=0.05)
    
    # Country breakdown reconciliation
    country_agg = aggregate_financial_by_dimension(financial_df, 'Country')
    assert np.isclose(country_agg['Net_Sales'].sum(), kpis['net_sales'], atol=0.05)
    assert np.isclose(country_agg['Profit'].sum(), kpis['total_profit'], atol=0.05)
    assert np.isclose(country_agg['COGS'].sum(), kpis['total_cogs'], atol=0.05)

def test_financial_scenario_simulation(financial_df):
    # Simulate 10% discount cut and 0% COGS change
    sim = simulate_financial_scenario(financial_df, discount_pct_delta=-0.10, cogs_pct_delta=0.0)
    baseline_profit = sim['baseline']['total_profit']
    sim_profit = sim['simulated']['total_profit']
    expected_profit_gain = sim['baseline']['total_discounts'] * 0.10
    
    assert np.isclose(sim['variance']['profit_dollar_impact'], expected_profit_gain, atol=0.05)
    assert sim_profit > baseline_profit
