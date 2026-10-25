# RISK Master Framework — Enterprise Data Analytics & Business Intelligence Suite

[![Quality Assurance: Pytest Verified](https://img.shields.io/badge/Test_Suite-20_Passed-emerald?style=for-the-badge&logo=pytest)](file:///tests/)
[![Data Pipeline: Deterministic & Reconciled](https://img.shields.io/badge/Data_Reconciliation-Zero_Variance-blue?style=for-the-badge&logo=python)](file:///reports/reconciliation_report.md)
[![BI Architecture: Kimball Star Schema](https://img.shields.io/badge/Power_BI-Star_Schema_DAX-gold?style=for-the-badge&logo=powerbi)](file:///powerbi/)

An enterprise, evidence-driven business intelligence and advanced data analytics suite integrating four commercial projects across retail merchandising, customer churn cohort dynamics, corporate financial accounting, and executive dashboard engineering.

Built upon the **RISK Framework**:
- **R — Requirements & Research**: Non-destructive data profiling, source inspection, schema validation, and anomaly discovery.
- **I — Investigation & Insight Discovery**: Descriptive statistics, elasticity analysis, cohort survival modeling, and managerial accounting decomposition.
- **S — Solution Engineering**: Modular Python data pipelines, automated Pytest testing suites, and normalized Kimball Star-Schema models.
- **K — Knowledge Delivery & KPI Validation**: Executive findings registers, prioritized retention playbooks, DAX measures, and zero-variance reconciliation audits.

---

## 1. Portfolio Architectural Overview

```
risk-data-intelligence-suite/
├── README.md                               # Consolidated Master Architecture & Executive Report
├── requirements.txt                        # Pinned analytical and testing dependencies
├── .gitignore                              # Clean Python, IDE, and temporary cache ignores
├── data/
│   ├── raw/                                # Raw, immutable source files from repository
│   │   ├── superstore_sales.csv            # 10,800 raw lines (including appended sheets)
│   │   ├── telco_customer_churn.csv        # 7,043 raw subscriber records
│   │   └── financial_sample.xlsx           # 700 raw corporate accounting records
│   └── processed/                          # Validated, clean, and modeled datasets
│       ├── superstore_cleaned.csv          # 9,994 validated retail transactions
│       ├── superstore_people.csv           # 4 regional territory managers
│       ├── superstore_returns.csv          # 296 unique order returns
│       ├── telco_churn_cleaned.csv         # 7,043 sanitized subscriber profiles with cohorts
│       ├── financial_sample_cleaned.csv    # 700 normalized financial records
│       └── star_schema/                    # Power BI Star Schema Dimension & Fact Tables
│           ├── FactSales.csv               # Fact table (9,994 line items)
│           ├── DimDate.csv                 # Continuous calendar (1,826 days; 2014-2018)
│           ├── DimCustomer.csv             # Conformed customer dimension (793 customers)
│           ├── DimProduct.csv              # Conformed product catalog (1,862 products)
│           └── DimGeography.csv            # Regional territory hierarchy (631 postal codes)
├── src/                                    # Reusable, single-responsibility Python engine
│   ├── __init__.py
│   ├── data_loader.py                      # Automated fetching and raw ingestion
│   ├── data_validation.py                  # Structural schema audit and anomaly detection
│   ├── data_cleaning.py                    # Deterministic anomaly resolution & cleaning
│   └── metrics.py                          # Centralized KPI calculations and scenario engines
├── notebooks/                              # Fully executed, reproducible Jupyter Notebooks
│   ├── 01_superstore_eda.ipynb             # Task 1: Exploratory Data Analysis & Merchandising
│   ├── 02_superstore_powerbi_prep.ipynb    # Task 2: Star-Schema Dimensional ETL & Reconciliation
│   ├── 03_customer_churn_analysis.ipynb    # Task 3: Customer Cohort Retention & Churn Analytics
│   └── 04_financial_analysis.ipynb         # Task 4: Corporate Financial & Margin Sensitivity
├── reports/                                # Formal executive documentation & visual assets
│   ├── data_quality/                       # Data dictionaries and forensic audit reports
│   │   ├── superstore_quality_report.md
│   │   ├── telco_quality_report.md
│   │   └── financial_quality_report.md
│   ├── figures/                            # High-DPI presentation charts (300 DPI)
│   │   ├── superstore/                     # 7 retail sales and profit figures
│   │   ├── churn/                          # 5 customer retention and cohort figures
│   │   └── financial/                      # 5 corporate finance and waterfall figures
│   ├── executive_findings.md               # 5+ retail merchandising findings & commercial actions
│   ├── churn_retention_recommendations.md  # Subscriber retention playbook & risk segment ledger
│   ├── financial_kpi_report.md             # Corporate income statement report & Enterprise deficit
│   ├── reconciliation_report.md            # Zero-variance Python vs. Power BI reconciliation
│   └── limitations.md                      # Transparent methodological controls & disclaimers
├── powerbi/                                # Native Power BI Specifications & DAX Models
│   ├── superstore_model.md                 # Star-schema relationships, keys, and cardinalities
│   ├── superstore_measures.dax             # Production DAX measures with continuous time-intelligence
│   ├── superstore_dashboard_spec.md        # 4-page executive dashboard layout specifications
│   ├── financial_model.md                  # Financial statement hierarchy and accounting rules
│   ├── financial_measures.dax              # Financial DAX and What-If scenario parameters
│   └── financial_dashboard_spec.md         # 3-page corporate financial dashboard specifications
└── tests/                                  # Automated Pytest Quality Assurance Suite
    ├── __init__.py
    ├── test_raw_schema.py                  # Raw dataset schema and structural baseline tests
    ├── test_data_quality.py                # Processed dataset clean assertions and boundaries
    ├── test_metrics.py                     # Mathematical invariance and reconciliation tests
    ├── test_powerbi_reconciliation.py      # Star Schema vs. Flat transaction reconciliation
    └── test_e2e_pipeline.py                # End-to-end integration and data flow tests
```

---

## 2. Forensic Anomaly Audit & Data Engineering Discoveries

During initial data inspection under Phase 1 of the RISK framework, real-world data engineering anomalies were forensically isolated and resolved:

| Dataset | Raw Discovered Anomaly | Business Impact | Deterministic Resolution Protocol |
| :--- | :--- | :--- | :--- |
| **Superstore Sales** | Rows 9,994 to 10,799 contain concatenated lookup tables (`Person/Region` and `Returned/Order ID`). | Blind date/numeric conversions fail with 806 null rows; duplicates inflated by 504. | Deconstructed into three clean artifacts: `superstore_cleaned.csv` (9,994 orders), `superstore_people.csv` (4 territory managers), and `superstore_returns.csv` (296 unique returns). |
| **Superstore Postal Codes** | 11 records in Burlington, Vermont have missing postal codes. | Map visual holes and broken geographic hierarchy. | Imputed with standard Burlington ZIP code `05401`. |
| **Telco Customer Churn** | `TotalCharges` stored as text with 11 whitespace strings (`' '`). | Fails numeric type-casting; causes pipeline crashes. | Cross-tabulation proved all 11 records have `tenure == 0` (brand-new accounts). Imputed with `0.0` and cast to `float64`. |
| **Financial Sample** | Column `' Sales'` contains a leading whitespace. `Discount Band` has 53 nulls. | Field lookup errors; `pd.read_csv` treats `'None'` as `NaN`. | Whitespace stripped across all columns; missing discount bands standardized to `'No Discount'`. |

---

## 3. Four Integrated BI Projects: Findings & Deliverables

### Task 1 — Superstore Retail Sales EDA
- **Deliverable**: [`notebooks/01_superstore_eda.ipynb`](file:///notebooks/01_superstore_eda.ipynb) | [`reports/executive_findings.md`](file:///reports/executive_findings.md)
- **Executive Findings Summary**:
  1. **The 20% Discount Cliff**: Discounts between 0% and 10% produce healthy margins (+27.9% and +14.8%). Discounts exceeding 20% cause severe profit destruction (-17.9% for 21–50% discounts, -87.8% for >50% discounts), destroying \$64,346 in profit.
  2. **Severe Sub-Category Loss Leaders**: Furniture generated only \$18,451 profit (2.5% margin), dragged down by Tables (-\$17,725 loss) and Bookcases (-\$3,473 loss).
  3. **Central Region Underperformance**: Central region accounts for 21.8% of sales but delivers only 13.9% of profit (7.9% margin vs. West's 14.9%) due to average discounts of 24.0% vs. West's 10.9%.
  4. **Holiday Q4 Seasonality**: November and December generate 31.4% of annual revenue and 33.8% of profit.
  5. **Corporate Margin Premium**: Corporate (13.0% margin) and Home Office (14.0% margin) accounts outperform Consumer retail (11.5%).

---

### Task 2 — Interactive Power BI Sales & Profit Dashboard
- **Deliverables**: [`powerbi/superstore_measures.dax`](file:///powerbi/superstore_measures.dax) | [`powerbi/superstore_model.md`](file:///powerbi/superstore_model.md) | [`powerbi/superstore_dashboard_spec.md`](file:///powerbi/superstore_dashboard_spec.md) | [`reports/reconciliation_report.md`](file:///reports/reconciliation_report.md)
- **Dimensional Modeling Architecture**:
  - Normalized Star Schema: `FactSales` (9,994 rows), `DimDate` (1,826 days), `DimCustomer` (793 customers), `DimProduct` (1,862 products), `DimGeography` (631 postal codes).
  - 100% referential integrity with zero orphan records.
  - Active continuous time-intelligence relationships enabling `DATEADD` and `TOTALYTD`.
- **Production DAX Measures**: `Total Sales`, `Total Profit`, `Profit Margin %`, `Total Orders`, `Average Order Value`, `Sales Previous Year`, `YoY Sales Growth %`, `Order Return Rate %`.
- **4 Dashboard Pages**:
  1. *Executive Overview*: Top-level KPIs, monthly trajectory, regional clustered bars, and category donut.
  2. *Product Profitability*: Sub-category treemap, sales vs. profit scatter, top 15 loss leaders table, and discount elasticity.
  3. *Customer & Regional Dynamics*: Customer segment breakdown, regional manager accountability, and top 20 customer Pareto table.
  4. *Trend & Variance Analysis*: Annual YoY variance waterfall, MoM growth trends, and calendar performance matrix.

---

### Task 3 — Customer Cohort & Churn Analytics (IBM Telco)
- **Deliverables**: [`notebooks/03_customer_churn_analysis.ipynb`](file:///notebooks/03_customer_churn_analysis.ipynb) | [`reports/churn_retention_recommendations.md`](file:///reports/churn_retention_recommendations.md)
- **Portfolio Baseline**: 7,043 customers, 26.54% churn rate (1,869 churned), Monthly Revenue Exposure = \$139,130.85/month (\$1.67M ARR).
- **Key Discoveries**:
  1. *Contract Structure*: Month-to-month contracts churn at **42.71%**, compared to 11.27% for One-Year and 2.83% for Two-Year contracts ($15.1\times$ risk factor).
  2. *First-Year Attrition*: 0–12 month cohort exhibits **47.44%** churn (1,037 accounts lost), accounting for 55.5% of total portfolio churn.
  3. *Fiber Optic Tech Support Deficit*: Fiber optic subscribers without tech support churn at **51.81%** vs. 27.60% with tech support.
  4. *Electronic Check Friction*: Customers paying via electronic check churn at **45.29%** vs. 15.24% for credit card auto-pay.
- **Actionable Commercial Retention Playbook**:
  - *Initiative 1*: Automated 6-month contract step-up incentive (\$10/mo credit for 3 months upon 12-month renewal; saves \$105.6k ARR).
  - *Initiative 2*: Auto-pay transition discount (\$2.50/mo discount for ACH/Card auto-pay; saves \$76.5k net ARR).
  - *Initiative 3*: Complimentary 90-day Fiber Care Priority Tech Support bundle (saves \$153.7k ARR).
  - **Net Annual Portfolio Benefit**: **+\$251,300 ARR** ($297\%$ ROI).

---

### Task 4 — Corporate Financial & Margin Performance
- **Deliverables**: [`notebooks/04_financial_analysis.ipynb`](file:///notebooks/04_financial_analysis.ipynb) | [`powerbi/financial_measures.dax`](file:///powerbi/financial_measures.dax) | [`reports/financial_kpi_report.md`](file:///reports/financial_kpi_report.md)
- **Consolidated Financial Statements**:
  - Gross Sales: \$127,931,598.50 ($100.0\%$)
  - Less Discounts: (\$9,205,248.24) ($7.20\%$ of Gross)
  - Net Sales: \$118,726,350.25 ($92.80\%$ of Gross)
  - Less COGS: (\$101,832,648.00) ($85.77\%$ of Net)
  - Operating Profit: **\$16,893,702.25** ($14.23\%$ Margin)
- **Key Managerial Discoveries**:
  1. *The Enterprise Deficit*: Enterprise segment generated \$19.61M net sales but suffered a **-\$616,900 net loss** (-3.15% margin) due to a 103.15% COGS absorption ratio.
  2. *Government Profit Engine*: Government delivered \$11.39M profit (21.69% margin), driving 67.4% of total company profit.
  3. *COGS Sensitivity Asymmetry*: Because COGS absorbs 85.77% of revenue, profitability is $5.5\times$ more sensitive to a 5% COGS inflation (-\$5.09M profit) than to a 5% discount shift.
- **What-If Scenario Modeling**: Parameterized sensitivity sliders for Discount adjustments ($\pm 30\%$) and COGS inflation ($\pm 20\%$) with dynamic DAX recalculations.

---

## 4. Reconciliation Matrix: Python vs. Power BI Model

All core financial, sales, and churn metrics were independently cross-audited between Python analytical scripts and the Power BI Star Schema data model:

| Metric Name | Python Aggregated Output | Power BI Star Schema Model | Variance | Audit Result |
| :--- | :--- | :--- | :--- | :--- |
| Superstore Total Sales | \$2,297,200.86 | \$2,297,200.86 | \$0.00 | **MATCH (Zero Variance)** |
| Superstore Total Profit | \$286,397.02 | \$286,397.02 | \$0.00 | **MATCH (Zero Variance)** |
| Superstore Profit Margin | 12.47% | 12.47% | 0.00% | **MATCH (Zero Variance)** |
| Superstore Total Quantity | 37,873 units | 37,873 units | 0 units | **MATCH (Zero Variance)** |
| Superstore Unique Orders | 5,009 orders | 5,009 orders | 0 orders | **MATCH (Zero Variance)** |
| Telco Total Customers | 7,043 accounts | 7,043 accounts | 0 accounts | **MATCH (Zero Variance)** |
| Telco Churn Rate % | 26.54% | 26.54% | 0.00% | **MATCH (Zero Variance)** |
| Financial Gross Sales | \$127,931,598.50 | \$127,931,598.50 | \$0.00 | **MATCH (Zero Variance)** |
| Financial Net Sales | \$118,726,350.25 | \$118,726,350.25 | \$0.00 | **MATCH (Zero Variance)** |
| Financial Operating Profit | \$16,893,702.25 | \$16,893,702.25 | \$0.00 | **MATCH (Zero Variance)** |

---

## 5. Automated Verification & Testing Suite

The repository contains an automated Pytest test suite covering schema validation, data cleaning assertions, mathematical invariance, star-schema joins, and end-to-end integration:

```bash
# Execute the complete automated test suite
pytest tests/ -v
```

### Test Suite Inventory (20 Automated Tests):
- `tests/test_raw_schema.py`: Asserts raw file structures, row counts, and detects source anomalies.
- `tests/test_data_quality.py`: Asserts zero nulls in cleaned critical columns, Burlington ZIP code repair, and numeric boundaries.
- `tests/test_metrics.py`: Asserts category and monthly sales reconciliations, churn denominator balance, and financial statement identities.
- `tests/test_powerbi_reconciliation.py`: Asserts zero variance across star schema joins and confirms zero orphan records.
- `tests/test_e2e_pipeline.py`: Tests end-to-end data flow from raw ingestion to final KPI calculations.

---

## 6. Execution & Reproducibility Guide

### Environment Setup
```bash
# Clone the repository via SSH
git clone git@github.com:rajeshwari229080/Datheon_Data_Analytics_-_Power_BI_Internship.git
cd Datheon_Data_Analytics_-_Power_BI_Internship

# Install dependencies
pip install -r requirements.txt
```

### Reproduce Data Pipeline & Star Schema
```bash
# Ingest and clean raw datasets
python src/data_cleaning.py

# Run test suite to verify pipeline integrity
pytest tests/ -v
```

### Run Analysis & Execute Notebooks
All Jupyter Notebooks in `notebooks/` are pre-executed with embedded tables and figures. To re-execute them head-to-tail:
```bash
jupyter nbconvert --to notebook --execute notebooks/01_superstore_eda.ipynb --inplace
jupyter nbconvert --to notebook --execute notebooks/02_superstore_powerbi_prep.ipynb --inplace
jupyter nbconvert --to notebook --execute notebooks/03_customer_churn_analysis.ipynb --inplace
jupyter nbconvert --to notebook --execute notebooks/04_financial_analysis.ipynb --inplace
```

---

## 7. Methodological Controls & Disclaimers
1. **Cross-Sectional vs. Longitudinal Panels**: Telco churn analysis represents a cross-sectional snapshot. Tenure cohorts reflect survivor distributions rather than true multi-year panel survival curves.
2. **Correlation vs. Causation**: Observed associations (e.g., electronic check and fiber optic churn) reflect customer segment profiles and must not be interpreted as proven causal drivers without controlled A/B testing.
3. **No Fabricated Budgets**: Because `financial_sample.xlsx` does not contain target or budget fields, performance is benchmarked against historical prior-year periods and simulated via parameterized What-If scenarios.
