"""
Unit tests asserting raw dataset schema and forensic integrity.
"""
import pytest
from src.data_loader import load_raw_superstore, load_raw_telco, load_raw_financial
from src.data_validation import (
    audit_dataset_structure,
    audit_superstore_anomalies,
    audit_telco_anomalies,
    audit_financial_anomalies,
    EXPECTED_SUPERSTORE_COLUMNS,
    EXPECTED_TELCO_COLUMNS,
    EXPECTED_FINANCIAL_COLUMNS
)

def test_raw_superstore_schema():
    df = load_raw_superstore()
    audit = audit_dataset_structure(df, EXPECTED_SUPERSTORE_COLUMNS, "Superstore")
    assert audit["total_rows"] == 10800
    assert audit["total_cols"] == 21
    assert audit["schema_valid"] is True
    
    anomalies = audit_superstore_anomalies(df)
    assert anomalies["appended_table_rows"] == 806
    assert anomalies["orders_row_count"] == 9994
    assert anomalies["burlington_missing_postal_codes"] == 11
    assert anomalies["exact_duplicates_in_orders"] == 0

def test_raw_telco_schema():
    df = load_raw_telco()
    audit = audit_dataset_structure(df, EXPECTED_TELCO_COLUMNS, "Telco")
    assert audit["total_rows"] == 7043
    assert audit["total_cols"] == 21
    assert audit["schema_valid"] is True
    
    anomalies = audit_telco_anomalies(df)
    assert anomalies["blank_total_charges"] == 11
    assert anomalies["zero_tenure_records"] == 11
    assert anomalies["unique_customer_ids"] == 7043

def test_raw_financial_schema():
    df = load_raw_financial()
    audit = audit_dataset_structure(df, EXPECTED_FINANCIAL_COLUMNS, "Financial")
    assert audit["total_rows"] == 700
    assert audit["total_cols"] == 16
    assert audit["schema_valid"] is True
    
    anomalies = audit_financial_anomalies(df)
    assert anomalies["has_leading_space_sales_col"] is True
    assert anomalies["null_discount_band_count"] == 53
    assert anomalies["unique_products"] == 6
    assert anomalies["unique_countries"] == 5
