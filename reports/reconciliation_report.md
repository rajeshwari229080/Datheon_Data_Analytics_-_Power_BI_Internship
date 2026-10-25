# Data Reconciliation & KPI Validation Report: Python vs. Power BI Model

## 1. Executive Summary & Verification Objective
As mandated by the **RISK Framework** (Knowledge Delivery & KPI Validation), this report provides independent mathematical reconciliation comparing aggregations derived from the cleaned flat transactional dataset against the normalized **Power BI Star Schema** (`FactSales`, `DimDate`, `DimCustomer`, `DimProduct`, `DimGeography`).

Every core measure was audited for invariance across all dimensional cuts:
- **Baseline Population**: 9,994 order line items.
- **Auditing Rule**: Aggregation variance must be strictly $\$0.00$ (zero tolerance for data loss or double counting).

---

## 2. Core Measure Reconciliation Audit

| KPI / Measure | Cleaned Flat Dataset (Python) | Power BI Star Schema Model | Absolute Variance | Reconciliation Status |
| :--- | :--- | :--- | :--- | :--- |
| **Total Sales ($)** | \$2,297,200.86 | \$2,297,200.86 | \$0.00 | **MATCH (100.0%)** |
| **Total Profit ($)** | \$286,397.02 | \$286,397.02 | \$0.00 | **MATCH (100.0%)** |
| **Profit Margin %** | 12.47% | 12.47% | 0.00% | **MATCH (100.0%)** |
| **Total Quantity** | 37,873 units | 37,873 units | 0 units | **MATCH (100.0%)** |
| **Total Unique Orders** | 5,009 orders | 5,009 orders | 0 orders | **MATCH (100.0%)** |
| **Average Order Value** | \$458.61 | \$458.61 | \$0.00 | **MATCH (100.0%)** |
| **Total Row Items** | 9,994 rows | 9,994 rows | 0 rows | **MATCH (100.0%)** |

---

## 3. Dimensional Category Reconciliation

| Category | Python Sales ($) | Star-Schema Sales ($) | Python Profit ($) | Star-Schema Profit ($) | Profit Margin % | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Technology** | \$836,154.03 | \$836,154.03 | \$145,454.81 | \$145,454.81 | 17.39% | MATCH |
| **Furniture** | \$741,999.80 | \$741,999.80 | \$18,451.27 | \$18,451.27 | 2.49% | MATCH |
| **Office Supplies** | \$719,047.03 | \$719,047.03 | \$122,490.94 | \$122,490.94 | 17.04% | MATCH |
| **Total Reconciled** | **\$2,297,200.86** | **\$2,297,200.86** | **\$286,397.02** | **\$286,397.02** | **12.47%** | **ZERO VARIANCE** |

---

## 4. Regional Hierarchy Reconciliation

| Region | Regional Manager | Sales ($) | Profit ($) | Profit Margin % | Regional Sales Share % | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **West** | Anna Andreadi | \$725,457.82 | \$108,418.45 | 14.94% | 31.58% | MATCH |
| **East** | Chuck Magee | \$678,781.24 | \$91,522.78 | 13.48% | 29.55% | MATCH |
| **Central** | Kelly Williams | \$501,239.89 | \$39,706.36 | 7.92% | 21.82% | MATCH |
| **South** | Cassandra Brandow | \$391,721.91 | \$46,749.43 | 11.93% | 17.05% | MATCH |
| **Total Reconciled** | — | **\$2,297,200.86** | **\$286,397.02** | **12.47%** | **100.00%** | **ZERO VARIANCE** |

---

## 5. Annual Time-Intelligence & YoY Sales Growth Reconciliation

| Calendar Year | Sales ($) | Prior Year Sales ($) | YoY Sales Growth ($) | YoY Sales Growth % | Profit ($) | Profit Margin % |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **2014** | \$484,247.50 | N/A (Baseline Year) | N/A | N/A | \$49,543.97 | 10.23% |
| **2015** | \$470,532.51 | \$484,247.50 | -\$13,714.99 | -2.83% | \$61,618.60 | 13.10% |
| **2016** | \$609,205.60 | \$470,532.51 | +\$138,673.09 | +29.47% | \$81,795.17 | 13.43% |
| **2017** | \$733,215.26 | \$609,205.60 | +\$124,009.66 | +20.36% | \$93,439.27 | 12.74% |
| **Total Portfolio** | **\$2,297,200.86** | — | — | — | **\$286,397.02** | **12.47%** |

*Note: Automated tests in `tests/test_powerbi_reconciliation.py` verify that `FactSales` merged with `DimDate` yields exact annual totals matching Python time-series aggregations.*

---

## 6. Audit Conclusion
1. **Mathematical Invariance**: Across all cuts (Total, Category, Region, Segment, and Year), variance is strictly $0.00$.
2. **Referential Integrity**: 100% of foreign keys in `FactSales` find a parent match in the respective dimension table. Zero orphan records exist.
3. **Continuous Calendar Compatibility**: `DimDate` spans 1,826 days from 2014-01-01 to 2018-12-31 without gaps, ensuring deterministic behavior of DAX functions `DATEADD` and `TOTALYTD`.
