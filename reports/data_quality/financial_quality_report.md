# Data Quality & Data Dictionary Report: Microsoft Financial Sample

## 1. Dataset Overview
- **Source File**: `data/raw/financial_sample.xlsx`
- **Official Source**: [Datheon Datasets](https://www.datheon.in/datasets/financial_sample.xlsx)
- **Sheet Name**: `Sheet1`
- **Raw Dimensions**: 700 rows × 16 columns
- **File Size**: 81.46 KB

---

## 2. Forensic Quality & Accounting Integrity Audit

### A. Column Header Whitespace Anomaly
- Column `' Sales'` contains a leading space in the raw Excel header.
- **Handling Protocol**: Strip all leading and trailing whitespace across all column names so `' Sales'` becomes `'Sales'`.

### B. Missing Values in `Discount Band`
- Exactly **53 rows** contain null in the `Discount Band` column.
- Cross-tabulation against `Discounts` confirms that all 53 rows have `Discounts == 0.0`.
- **Handling Protocol**: Impute missing `Discount Band` values with `'None'`.

### C. Accounting Mathematical Reconciliation
Every record was tested for fundamental managerial accounting identities:
1. $\text{Gross Sales} = \text{Units Sold} \times \text{Sale Price}$
2. $\text{Net Sales} = \text{Gross Sales} - \text{Discounts}$
3. $\text{COGS} = \text{Units Sold} \times \text{Manufacturing Price}$ (or designated base cost)
4. $\text{Profit} = \text{Net Sales} - \text{COGS}$
- **Reconciliation Audit**: In the dataset, the accounting identity $\text{Gross Sales} - \text{Discounts} = \text{Sales}$ holds exactly to the cent ($0.00$ variance across all 700 rows).

---

## 3. Data Dictionary

| Column Name | Raw Type | Cleaned Type | Null Count | Description & Business Meaning |
| :--- | :--- | :--- | :--- | :--- |
| `Segment` | String | Category | 0 | Commercial customer segment (Government, Small Business, Enterprise, Midmarket, Channel Partners). |
| `Country` | String | Category | 0 | Sovereign operating market (Canada, Germany, France, Mexico, United States of America). |
| `Product` | String | Category | 0 | Commercial product line (Carretera, Montana, Paseo, Velo, VTT, Amarilla). |
| `Discount Band` | String | Category | 53 (None) | Tier of promotional discount applied: None, Low, Medium, High. |
| `Units Sold` | Float64 | Float64 | 0 | Total physical volume of units shipped. |
| `Manufacturing Price` | Int64 | Float64 | 0 | Standardized factory production cost per unit ($). |
| `Sale Price` | Int64 | Float64 | 0 | List / contract sales price per unit before discounts ($). |
| `Gross Sales` | Float64 | Float64 | 0 | Top-line transaction revenue before discount deduction ($). |
| `Discounts` | Float64 | Float64 | 0 | Value of commercial discounts conceded to customer ($). |
| `Sales` | Float64 | Float64 | 0 | Net revenue realized after discount deductions ($). |
| `COGS` | Float64 | Float64 | 0 | Total Cost of Goods Sold incurred for the order ($). |
| `Profit` | Float64 | Float64 | 0 | Net operating margin / contribution profit realized ($). |
| `Date` | Datetime64 | Datetime64 | 0 | Transaction accounting date (2013-09-01 to 2014-12-01). |
| `Month Number` | Int64 | Int64 | 0 | Calendar month integer (1 to 12). |
| `Month Name` | String | Category | 0 | Calendar month string (January to December). |
| `Year` | Int64 | Int64 | 0 | Calendar accounting year (2013, 2014). |
