# Power BI Executive Dashboard Specification: Superstore Sales & Profit

## 1. Executive Design System & Visual Guidelines
- **Canvas Resolution**: 16:9 widescreen ($1920 \times 1080$ px).
- **Color Palette (WCAG 2.1 AA Compliant)**:
  - Primary Corporate Navy: `#0F172A` (Header, card labels, dark accents)
  - Accent / Primary Measure: `#2563EB` (Total Sales, positive volume)
  - Success / Margin Accent: `#059669` (Total Profit, positive YoY growth)
  - Danger / Loss Accent: `#DC2626` (Negative profit, loss leaders, high discount erosion)
  - Background Neutral: `#F8FAFC` (Canvas background)
  - Card & Container Surface: `#FFFFFF` with subtle border `#E2E8F0` and shadow
- **Typography**:
  - Title: Segoe UI Bold, 20pt
  - KPI Callout Values: Segoe UI Bold, 28pt
  - Section Headers: Segoe UI Semibold, 13pt
  - Data Labels & Tables: Segoe UI Regular, 10pt

---

## 2. Page 1 — Executive Overview

### A. Purpose
Provides C-suite executives with immediate visibility into top-line sales, bottom-line net profit, overall profit margin %, order volume, and geographic/categorical contribution.

### B. Visual Layout & Coordinates
1. **Top KPI Header Strip** (4 Cards, $Y=40$, Height=110):
   - **Card 1**: `[Total Sales]` — Formatted as Currency (`$#,##0`), Secondary subtitle showing `[YoY Sales Growth %]`.
   - **Card 2**: `[Total Profit]` — Formatted as Currency (`$#,##0`), Secondary subtitle showing `[YoY Profit Growth %]`.
   - **Card 3**: `[Profit Margin %]` — Formatted as Percentage (`0.0%`), Conditional font color (Green $>12\%$, Red $<5\%$).
   - **Card 4**: `[Total Orders]` — Formatted as Integer (`#,##0`), alongside `[Average Order Value]`.
2. **Global Slicer Panel** (Top Right, $Y=40$, $X=1500$, Width=380):
   - Dropdown Slicers: `DimDate[Year]`, `DimGeography[Region]`, `DimCustomer[Segment]`.
3. **Monthly Sales & Profit Trajectory** (Line and Clustered Column Chart, $Y=170$, $X=40$, Width=1180, Height=420):
   - X-Axis: `DimDate[MonthYear]`
   - Column Values: `[Total Sales]` (Cobalt Blue `#2563EB`)
   - Line Values: `[Total Profit]` (Emerald Green `#059669`)
4. **Category Contribution** (Donut Chart, $Y=170$, $X=1240$, Width=640, Height=420):
   - Legend: `DimProduct[Category]`
   - Values: `[Total Sales]`
   - Tooltips: `[Total Profit]`, `[Profit Margin %]`
5. **Regional Sales & Profit Matrix** (Clustered Bar Chart, $Y=610$, $X=40$, Width=920, Height=430):
   - Y-Axis: `DimGeography[Region]`
   - Values: `[Total Sales]`, `[Total Profit]`
   - Tooltips: `DimGeography[Regional Manager]`, `[Profit Margin %]`
6. **Executive Takeaways Card** (Formatted Markdown Card, $Y=610$, $X=980$, Width=900, Height=430):
   - Highlights 20% discount cliff, top performing West region ($14.9\%$ margin), and seasonal Q4 surge.

---

## 3. Page 2 — Product Profitability & Loss Leader Audit

### A. Purpose
Enables Chief Commercial Officers and Merchandising Managers to pinpoint value destruction, evaluate sub-category profitability, and eliminate loss leaders.

### B. Visual Layout
1. **Sub-Category Treemap** (Left, Width=900, Height=480):
   - Group: `DimProduct[Category]`
   - Details: `DimProduct[Sub-Category]`
   - Size: `[Total Sales]`
   - Color Saturation: `[Total Profit]` (Diverging gradient: Red for negative profit $\le 0$, Green for positive profit $> \$20k$).
2. **Sales vs. Profit Scatter Plot** (Right, Width=940, Height=480):
   - X-Axis: `[Total Sales]`
   - Y-Axis: `[Total Profit]`
   - Details: `DimProduct[Product Name]`
   - Reference Lines: Constant line at $Y = 0$ (Breakeven line).
3. **Top 15 Loss Leaders Table** (Bottom Left, Width=980, Height=480):
   - Columns: `DimProduct[Product Name]`, `DimProduct[Sub-Category]`, `[Total Sales]`, `[Total Profit]`, `[Average Discount Rate %]`, `[Profit Margin %]`.
   - Sort: `[Total Profit]` Ascending. Conditional red data bars on Profit.
4. **Discount Band Impact on Margins** (Bottom Right, Width=860, Height=480):
   - X-Axis: `FactSales[Discount Band]`
   - Column Values: `[Profit Margin %]`
   - Highlight: Visually demarcating $>20\%$ discount cliff where margin turns steeply negative ($-17.9\%$ to $-87.8\%$).

---

## 4. Page 3 — Customer & Regional Dynamics

### A. Purpose
Analyzes customer concentration, purchasing patterns across Consumer, Corporate, and Home Office segments, and regional manager accountability.

### B. Visual Layout
1. **Segment Performance Matrix** (Top Left, Width=880, Height=360):
   - Columns: `DimCustomer[Segment]`, `[Total Sales]`, `[Total Profit]`, `[Total Orders]`, `[Average Order Value]`, `[Profit Margin %]`.
2. **Regional Margin Comparison** (Top Right, Width=960, Height=360):
   - Column Chart: `DimGeography[Region]` on X-Axis, `[Profit Margin %]` on Y-Axis.
   - Reference Line: Average company margin ($12.47\%$).
3. **Top 20 Customers by Revenue (Pareto Analysis)** (Bottom Left, Width=1050, Height=560):
   - Table: `DimCustomer[Customer Name]`, `DimCustomer[Segment]`, `[Total Sales]`, `[Total Profit]`, `[Total Orders]`, `[Sales Contribution %]`.
4. **Order Return Rate by Region & Shipping Mode** (Bottom Right, Width=790, Height=560):
   - Clustered Column: `DimGeography[Region]` on X-Axis, `FactSales[Ship Mode]` in Legend, `[Order Return Rate %]` on Y-Axis.

---

## 5. Page 4 — Trend & Variance Analysis

### A. Purpose
Provides finance and FP&A teams with Year-over-Year (YoY) variance breakdowns, month-over-month shifts, and calendar seasonality tracking.

### B. Visual Layout
1. **Annual YoY Sales & Profit Variance Waterfall** (Top Left, Width=920, Height=450):
   - Breakdown of annual sales progression from 2014 through 2017.
   - Measures: `[Sales Previous Year]`, `[Sales YoY Growth $]`, `[Total Sales]`.
2. **MoM Growth Percentage Line Chart** (Top Right, Width=920, Height=450):
   - X-Axis: `DimDate[MonthYear]`
   - Y-Axis: `[MoM Sales Growth %]`, `[YoY Sales Growth %]`
   - Visual Markers: Shaded band highlighting Q4 surge (November/December).
3. **Detailed Financial Performance Matrix** (Bottom, Width=1840, Height=470):
   - Hierarchy: `DimDate[Year]` -> `DimDate[QuarterName]` -> `DimDate[MonthName]`.
   - Values: `[Total Sales]`, `[Sales Previous Year]`, `[YoY Sales Growth %]`, `[Total Profit]`, `[Profit Previous Year]`, `[YoY Profit Growth %]`, `[Profit Margin %]`.

---

## 6. Step-by-Step Desktop Build Guide
1. Launch Power BI Desktop.
2. Select **Get Data** -> **Text/CSV**, navigate to `data/processed/star_schema/`, and import all 5 CSV files.
3. In Model View, establish relationships matching `powerbi/superstore_model.md`.
4. Right-click `FactSales` (or create a `_Measures` table) and paste the DAX definitions from `powerbi/superstore_measures.dax`.
5. Set formatting strings for each measure (Currency for Sales/Profit, Percentage for Margins/Growth).
6. Build the 4 pages following the visual coordinates and properties detailed above.
