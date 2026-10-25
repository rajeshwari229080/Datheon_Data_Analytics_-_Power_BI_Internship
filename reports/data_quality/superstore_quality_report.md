# Data Quality & Data Dictionary Report: Superstore Retail Sales

## 1. Dataset Overview
- **Source File**: `data/raw/superstore_sales.csv`
- **Official Source**: [Datheon Datasets](https://www.datheon.in/datasets/superstore_sales.csv)
- **Raw Dimensions**: 10,800 rows × 21 columns
- **File Size**: 2,240.00 KB
- **Encoding**: `latin1`

---

## 2. Forensic Anomaly Audit & Discovery

### A. Appended Multi-Table Anomaly (Critical Finding)
During row-level inspection, rows 9,994 to 10,799 were discovered to contain separate, concatenated tables rather than transaction records:
1. **Row 0 to 9993**: 9,994 retail sales line items.
2. **Row 9994**: Header row containing `Person` in `Row ID` and `Region` in `Order ID`.
3. **Rows 9995 to 9998**: Regional Managers lookup (Anna Andreadi - West, Chuck Magee - East, Kelly Williams - Central, Cassandra Brandow - South).
4. **Row 9999**: Header row containing `Returned` in `Row ID` and `Order ID` in `Order ID`.
5. **Rows 10000 to 10799**: 800 order return status entries (`Yes`, `Order ID`).

### B. Missing Values
- In the valid transactions slice (rows 0–9993), exactly 11 records have a missing `Postal Code`.
- All 11 records originate from **Burlington, Vermont** (US ZIP `05401`).
- Imputation Rule: Imputed with standard Burlington ZIP `05401`.

### C. Duplicates
- Raw file contains 504 duplicate rows, which originate strictly within the appended returns table.
- The transactions slice (rows 0–9993) contains **0 duplicate rows** across all 21 columns.

---

## 3. Data Dictionary (Transactions Table)

| Column Name | Raw Type | Cleaned Type | Null Count | Description & Business Meaning |
| :--- | :--- | :--- | :--- | :--- |
| `Row ID` | String | Integer | 0 | Unique sequential line item identifier (1 to 9994). |
| `Order ID` | String | String | 0 | Business identifier for an order (e.g., `CA-2017-152156`). |
| `Order Date` | String | Datetime64 | 0 | Date the transaction was placed by the customer. |
| `Ship Date` | String | Datetime64 | 0 | Date the order was fulfilled and shipped. |
| `Ship Mode` | String | Category | 0 | Shipping class: First Class, Same Day, Second Class, Standard Class. |
| `Customer ID` | String | String | 0 | Unique customer identifier (e.g., `CG-12520`). |
| `Customer Name` | String | String | 0 | Full legal name of the purchaser. |
| `Segment` | String | Category | 0 | Market segment: Consumer, Corporate, Home Office. |
| `Country` | String | Category | 0 | Country of transaction (United States). |
| `City` | String | String | 0 | Destination delivery city. |
| `State` | String | String | 0 | Destination delivery state / territory. |
| `Postal Code` | Float64 | String (5-digit) | 11 | Destination delivery 5-digit ZIP code (imputed for Burlington VT). |
| `Region` | String | Category | 0 | Geographic commercial territory: Central, East, South, West. |
| `Product ID` | String | String | 0 | Unique product SKU identifier (e.g., `FUR-BO-10001798`). |
| `Category` | String | Category | 0 | High-level merchandise category: Furniture, Office Supplies, Technology. |
| `Sub-Category` | String | Category | 0 | Detailed product grouping (17 sub-categories, e.g., Chairs, Binders). |
| `Product Name` | String | String | 0 | Full descriptive product catalog title. |
| `Sales` | Float64 | Float64 | 0 | Monetary transaction value in USD ($). |
| `Quantity` | Float64 | Integer | 0 | Number of units purchased. |
| `Discount` | Float64 | Float64 | 0 | Promotional discount applied (0.00 to 0.80). |
| `Profit` | Float64 | Float64 | 0 | Net operating margin / commercial profit in USD ($). |

---

## 4. Derived & Extracted Tables

1. **`superstore_cleaned.csv`**: Contains the 9,994 transaction rows with imputed postal codes, validated dates, and standardized types.
2. **`superstore_returns.csv`**: Contains 800 order return records with `Order ID` and `Returned = 'Yes'`.
3. **`superstore_people.csv`**: Contains 4 regional territory managers mapped to `Region`.
