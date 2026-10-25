# Data Quality & Data Dictionary Report: IBM Telco Customer Churn

## 1. Dataset Overview
- **Source File**: `data/raw/telco_customer_churn.csv`
- **Official Source**: [Datheon Datasets](https://www.datheon.in/datasets/telco_customer_churn.csv)
- **Raw Dimensions**: 7,043 rows × 21 columns
- **File Size**: 947.71 KB
- **Encoding**: UTF-8

---

## 2. Forensic Quality & Integrity Audit

### A. Blank String Numeric Anomaly (`TotalCharges`)
- Column `TotalCharges` is stored as an `object` string type in the raw CSV.
- Exactly **11 records** contain whitespace string `' '`.
- Cross-tabulation reveals that all 11 records have `tenure == 0`, representing brand-new subscribers who have not yet received their first monthly invoice.
- **Handling Protocol**: Impute `TotalCharges = 0.0` for all 11 records with zero tenure, then convert the series to `float64`.

### B. Customer ID Uniqueness
- Unique `customerID` count = 7,043 out of 7,043 rows (100% uniqueness).
- Zero duplicate rows across the entire dataset.

### C. Data Representation Consistency
- `SeniorCitizen` is represented as binary integer `0` / `1`.
- All other categorical flags (`Partner`, `Dependents`, `PhoneService`, `PaperlessBilling`, `Churn`) use `'Yes'` / `'No'`.
- Normalized mappings created to maintain consistency across statistical models and visualizations.

---

## 3. Data Dictionary

| Column Name | Raw Type | Cleaned Type | Null/Blank | Description & Business Meaning |
| :--- | :--- | :--- | :--- | :--- |
| `customerID` | String | String | 0 | Unique customer alphanumeric identifier. |
| `gender` | String | Category | 0 | Customer biological gender (Female, Male). |
| `SeniorCitizen` | Int64 | Category (0/1) | 0 | Binary indicator if customer is $\ge 65$ years old. |
| `Partner` | String | Category (Yes/No) | 0 | Whether the subscriber has a domestic partner. |
| `Dependents` | String | Category (Yes/No) | 0 | Whether the subscriber has dependent family members. |
| `tenure` | Int64 | Int64 | 0 | Number of elapsed months customer has subscribed. |
| `PhoneService` | String | Category (Yes/No) | 0 | Whether the customer subscribes to fixed wireline phone. |
| `MultipleLines` | String | Category | 0 | Single, Multiple, or No phone service. |
| `InternetService` | String | Category | 0 | Connection type: DSL, Fiber optic, No internet. |
| `OnlineSecurity` | String | Category | 0 | Value-added cybersecurity add-on (Yes/No/No internet). |
| `OnlineBackup` | String | Category | 0 | Cloud backup data storage add-on (Yes/No/No internet). |
| `DeviceProtection` | String | Category | 0 | Hardware insurance and warranty coverage. |
| `TechSupport` | String | Category | 0 | Dedicated tier-2 technical support service. |
| `StreamingTV` | String | Category | 0 | Digital TV streaming package add-on. |
| `StreamingMovies` | String | Category | 0 | Digital movie streaming entertainment package. |
| `Contract` | String | Category | 0 | Billing commitment: Month-to-month, One year, Two year. |
| `PaperlessBilling` | String | Category (Yes/No) | 0 | Electronic paperless invoice delivery. |
| `PaymentMethod` | String | Category | 0 | Payment settlement channel (Electronic check, Mailed check, Bank transfer, Credit card). |
| `MonthlyCharges` | Float64 | Float64 | 0 | Current monthly subscription fee billed in USD ($). |
| `TotalCharges` | String | Float64 | 11 blanks | Cumulative revenue billed across subscriber tenure in USD ($). |
| `Churn` | String | Category (Yes/No) | 0 | Retention outcome: Did the customer leave within the last month? |
