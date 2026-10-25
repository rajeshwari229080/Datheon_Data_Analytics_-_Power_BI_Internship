"""
Centralized Business Intelligence & Analytical Metrics Engine
Provides validated mathematical calculations and aggregations for:
1. Superstore Retail Sales & Profit
2. IBM Telco Customer Cohort & Churn
3. Corporate Financial & Margin Performance
"""
import sys
from pathlib import Path
from typing import Dict, Any, List
import pandas as pd
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# ==============================================================================
# 1. SUPERSTORE RETAIL SALES METRICS
# ==============================================================================

def calculate_superstore_kpis(df: pd.DataFrame) -> Dict[str, float]:
    """Calculate core high-level retail executive KPIs."""
    total_sales = float(df['Sales'].sum())
    total_profit = float(df['Profit'].sum())
    total_quantity = int(df['Quantity'].sum())
    total_orders = int(df['Order ID'].nunique())
    profit_margin_pct = (total_profit / total_sales * 100.0) if total_sales > 0 else 0.0
    aov = (total_sales / total_orders) if total_orders > 0 else 0.0
    
    return {
        "total_sales": round(total_sales, 2),
        "total_profit": round(total_profit, 2),
        "total_quantity": total_quantity,
        "total_orders": total_orders,
        "profit_margin_pct": round(profit_margin_pct, 2),
        "average_order_value": round(aov, 2)
    }

def aggregate_superstore_by_dimension(df: pd.DataFrame, dimension: str) -> pd.DataFrame:
    """Aggregate sales, profit, quantity, and margins by a specified categorical dimension."""
    agg = df.groupby(dimension).agg(
        Sales=('Sales', 'sum'),
        Profit=('Profit', 'sum'),
        Quantity=('Quantity', 'sum'),
        Orders=('Order ID', 'nunique')
    ).reset_index()
    
    agg['Sales'] = agg['Sales'].round(2)
    agg['Profit'] = agg['Profit'].round(2)
    agg['Profit_Margin_Pct'] = np.where(agg['Sales'] > 0, (agg['Profit'] / agg['Sales'] * 100).round(2), 0.0)
    agg['Sales_Share_Pct'] = (agg['Sales'] / agg['Sales'].sum() * 100).round(2)
    return agg.sort_values(by='Sales', ascending=False).reset_index(drop=True)

def aggregate_superstore_monthly(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate performance monthly across calendar periods."""
    monthly = df.groupby('Order YearMonth').agg(
        Sales=('Sales', 'sum'),
        Profit=('Profit', 'sum'),
        Quantity=('Quantity', 'sum'),
        Orders=('Order ID', 'nunique')
    ).reset_index()
    
    monthly['Sales'] = monthly['Sales'].round(2)
    monthly['Profit'] = monthly['Profit'].round(2)
    monthly['Profit_Margin_Pct'] = np.where(monthly['Sales'] > 0, (monthly['Profit'] / monthly['Sales'] * 100).round(2), 0.0)
    return monthly.sort_values(by='Order YearMonth').reset_index(drop=True)

def analyze_discount_elasticity(df: pd.DataFrame) -> pd.DataFrame:
    """Analyze the relationship between promotional discount bands and realized profit margins."""
    discount_agg = df.groupby('Discount Band', observed=True).agg(
        Order_Lines=('Row ID', 'count'),
        Total_Sales=('Sales', 'sum'),
        Total_Profit=('Profit', 'sum'),
        Avg_Discount=('Discount', 'mean')
    ).reset_index()
    
    discount_agg['Total_Sales'] = discount_agg['Total_Sales'].round(2)
    discount_agg['Total_Profit'] = discount_agg['Total_Profit'].round(2)
    discount_agg['Avg_Discount_Pct'] = (discount_agg['Avg_Discount'] * 100).round(2)
    discount_agg['Profit_Margin_Pct'] = np.where(
        discount_agg['Total_Sales'] > 0,
        (discount_agg['Total_Profit'] / discount_agg['Total_Sales'] * 100).round(2),
        0.0
    )
    return discount_agg

# ==============================================================================
# 2. TELCO CUSTOMER CHURN & COHORT METRICS
# ==============================================================================

def calculate_telco_churn_kpis(df: pd.DataFrame) -> Dict[str, float]:
    """Calculate overall churn and retention baseline KPIs."""
    total_customers = int(len(df))
    churned_customers = int(df['Churn_Numeric'].sum())
    retained_customers = total_customers - churned_customers
    churn_rate_pct = (churned_customers / total_customers * 100.0) if total_customers > 0 else 0.0
    retention_rate_pct = 100.0 - churn_rate_pct
    
    return {
        "total_customers": total_customers,
        "churned_customers": churned_customers,
        "retained_customers": retained_customers,
        "churn_rate_pct": round(churn_rate_pct, 2),
        "retention_rate_pct": round(retention_rate_pct, 2),
        "total_monthly_revenue": round(float(df['MonthlyCharges'].sum()), 2),
        "churned_monthly_revenue": round(float(df[df['Churn_Numeric'] == 1]['MonthlyCharges'].sum()), 2)
    }

def calculate_tenure_cohort_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Compute cross-sectional cohort churn and retention profiles by tenure buckets."""
    cohort = df.groupby('Tenure Cohort', observed=True).agg(
        Total_Customers=('customerID', 'count'),
        Churned_Customers=('Churn_Numeric', 'sum'),
        Avg_Monthly_Charges=('MonthlyCharges', 'mean'),
        Total_Monthly_Charges=('MonthlyCharges', 'sum')
    ).reset_index()
    
    cohort['Retained_Customers'] = cohort['Total_Customers'] - cohort['Churned_Customers']
    cohort['Churn_Rate_Pct'] = (cohort['Churned_Customers'] / cohort['Total_Customers'] * 100).round(2)
    cohort['Retention_Rate_Pct'] = (100.0 - cohort['Churn_Rate_Pct']).round(2)
    cohort['Avg_Monthly_Charges'] = cohort['Avg_Monthly_Charges'].round(2)
    cohort['Customer_Share_Pct'] = (cohort['Total_Customers'] / cohort['Total_Customers'].sum() * 100).round(2)
    
    return cohort

def calculate_segment_churn(df: pd.DataFrame, segment_col: str) -> pd.DataFrame:
    """Calculate customer count, churn count, and churn rate % across categorical segments."""
    seg = df.groupby(segment_col).agg(
        Total_Customers=('customerID', 'count'),
        Churned_Customers=('Churn_Numeric', 'sum'),
        Avg_Monthly_Charges=('MonthlyCharges', 'mean')
    ).reset_index()
    
    seg['Retained_Customers'] = seg['Total_Customers'] - seg['Churned_Customers']
    seg['Churn_Rate_Pct'] = (seg['Churned_Customers'] / seg['Total_Customers'] * 100).round(2)
    seg['Retention_Rate_Pct'] = (100.0 - seg['Churn_Rate_Pct']).round(2)
    seg['Avg_Monthly_Charges'] = seg['Avg_Monthly_Charges'].round(2)
    return seg.sort_values(by='Churn_Rate_Pct', ascending=False).reset_index(drop=True)

# ==============================================================================
# 3. CORPORATE FINANCIAL & MARGIN PERFORMANCE METRICS
# ==============================================================================

def calculate_financial_kpis(df: pd.DataFrame) -> Dict[str, float]:
    """Calculate executive corporate financial statement totals and margins."""
    gross_sales = float(df['Gross Sales'].sum())
    total_discounts = float(df['Discounts'].sum())
    net_sales = float(df['Sales'].sum())
    total_cogs = float(df['COGS'].sum())
    total_profit = float(df['Profit'].sum())
    units_sold = float(df['Units Sold'].sum())
    
    gross_profit_pct = (total_profit / net_sales * 100.0) if net_sales > 0 else 0.0
    cogs_ratio_pct = (total_cogs / net_sales * 100.0) if net_sales > 0 else 0.0
    discount_impact_pct = (total_discounts / gross_sales * 100.0) if gross_sales > 0 else 0.0
    
    return {
        "gross_sales": round(gross_sales, 2),
        "total_discounts": round(total_discounts, 2),
        "net_sales": round(net_sales, 2),
        "total_cogs": round(total_cogs, 2),
        "total_profit": round(total_profit, 2),
        "units_sold": round(units_sold, 2),
        "gross_profit_margin_pct": round(gross_profit_pct, 2),
        "cogs_ratio_pct": round(cogs_ratio_pct, 2),
        "discount_impact_pct": round(discount_impact_pct, 2)
    }

def aggregate_financial_by_dimension(df: pd.DataFrame, dimension: str) -> pd.DataFrame:
    """Aggregate financial statements by Segment, Country, or Product."""
    agg = df.groupby(dimension).agg(
        Units_Sold=('Units Sold', 'sum'),
        Gross_Sales=('Gross Sales', 'sum'),
        Discounts=('Discounts', 'sum'),
        Net_Sales=('Sales', 'sum'),
        COGS=('COGS', 'sum'),
        Profit=('Profit', 'sum')
    ).reset_index()
    
    for c in ['Gross_Sales', 'Discounts', 'Net_Sales', 'COGS', 'Profit']:
        agg[c] = agg[c].round(2)
        
    agg['Gross_Profit_Margin_Pct'] = np.where(agg['Net_Sales'] > 0, (agg['Profit'] / agg['Net_Sales'] * 100).round(2), 0.0)
    agg['COGS_Ratio_Pct'] = np.where(agg['Net_Sales'] > 0, (agg['COGS'] / agg['Net_Sales'] * 100).round(2), 0.0)
    agg['Discount_Impact_Pct'] = np.where(agg['Gross_Sales'] > 0, (agg['Discounts'] / agg['Gross_Sales'] * 100).round(2), 0.0)
    
    return agg.sort_values(by='Net_Sales', ascending=False).reset_index(drop=True)

def simulate_financial_scenario(
    df: pd.DataFrame,
    discount_pct_delta: float = 0.0,
    cogs_pct_delta: float = 0.0
) -> Dict[str, Any]:
    """
    Perform What-If financial scenario analysis.
    
    Args:
        df: Processed financial dataframe.
        discount_pct_delta: Percentage shift in discounts (e.g., -0.10 for 10% discount reduction).
        cogs_pct_delta: Percentage shift in COGS (e.g., +0.05 for 5% cost inflation).
        
    Returns:
        Dict comparing Baseline vs Simulated scenario metrics and dollar impact.
    """
    baseline = calculate_financial_kpis(df)
    
    # Simulation logic
    sim_gross_sales = baseline["gross_sales"]
    sim_discounts = baseline["total_discounts"] * (1.0 + discount_pct_delta)
    sim_net_sales = sim_gross_sales - sim_discounts
    sim_cogs = baseline["total_cogs"] * (1.0 + cogs_pct_delta)
    sim_profit = sim_net_sales - sim_cogs
    sim_margin = (sim_profit / sim_net_sales * 100.0) if sim_net_sales > 0 else 0.0
    
    profit_impact = sim_profit - baseline["total_profit"]
    margin_impact_pct = sim_margin - baseline["gross_profit_margin_pct"]
    
    return {
        "parameters": {
            "discount_pct_delta": discount_pct_delta,
            "cogs_pct_delta": cogs_pct_delta
        },
        "baseline": baseline,
        "simulated": {
            "gross_sales": round(sim_gross_sales, 2),
            "total_discounts": round(sim_discounts, 2),
            "net_sales": round(sim_net_sales, 2),
            "total_cogs": round(sim_cogs, 2),
            "total_profit": round(sim_profit, 2),
            "gross_profit_margin_pct": round(sim_margin, 2)
        },
        "variance": {
            "profit_dollar_impact": round(profit_impact, 2),
            "margin_point_impact": round(margin_impact_pct, 2)
        }
    }
