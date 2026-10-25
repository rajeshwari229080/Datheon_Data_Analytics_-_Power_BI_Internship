"""
End-to-End Pipeline Integration Test
Verifies deterministic data flow across ingestion, cleaning, star-schema modeling, and KPI calculation.
"""
import pytest
import pandas as pd
import numpy as np
from pathlib import Path

from src.data_loader import load_raw_superstore, load_raw_telco, load_raw_financial
from src.data_cleaning import clean_superstore, clean_telco, clean_financial
from src.metrics import (
    calculate_superstore_kpis,
    calculate_telco_churn_kpis,
    calculate_financial_kpis
)

def test_e2e_superstore_pipeline():
    orders_df, people_df, returns_df = clean_superstore()
    assert len(orders_df) == 9994
    assert len(people_df) == 4
    assert len(returns_df) > 0
    
    kpis = calculate_superstore_kpis(orders_df)
    assert kpis['total_sales'] == 2297200.86
    assert kpis['total_profit'] == 286397.02
    assert kpis['profit_margin_pct'] == 12.47

def test_e2e_telco_pipeline():
    telco_df = clean_telco()
    assert len(telco_df) == 7043
    assert telco_df['TotalCharges'].isnull().sum() == 0
    
    kpis = calculate_telco_churn_kpis(telco_df)
    assert kpis['total_customers'] == 7043
    assert kpis['churned_customers'] == 1869
    assert kpis['churn_rate_pct'] == 26.54

def test_e2e_financial_pipeline():
    fin_df = clean_financial()
    assert len(fin_df) == 700
    assert 'Sales' in fin_df.columns
    
    kpis = calculate_financial_kpis(fin_df)
    assert kpis['gross_sales'] == 127931598.50
    assert kpis['net_sales'] == 118726350.25
    assert kpis['total_profit'] == 16893702.25
