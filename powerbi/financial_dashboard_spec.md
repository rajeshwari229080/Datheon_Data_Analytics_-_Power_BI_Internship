# Power BI Financial Dashboard Specification: Corporate Margin Performance

## 1. Visual Design System
- **Theme Palette**:
  - Primary Corporate Navy: `#0F172A`
  - Revenue Accent: `#1E40AF`
  - COGS / Expense Accent: `#DC2626`
  - Profit / Surplus Accent: `#059669`
  - Surface Background: `#F8FAFC`
- **Canvas Aspect**: 16:9 ($1920 \times 1080$ px).

---

## 2. Page 1 — Financial Executive Overview

### A. Purpose
Provides executive leadership with a consolidated view of top-line gross revenue, commercial discount concessions, net sales, operating profit, and regional distribution.

### B. Visual Layout
1. **Top KPI Strip** (5 Cards across top):
   - **Card 1**: `[Gross Sales]` (\$127.93M)
   - **Card 2**: `[Total Discounts]` (\$9.21M, Concession: 7.20%)
   - **Card 3**: `[Net Sales]` (\$118.73M)
   - **Card 4**: `[Total Profit]` (\$16.89M)
   - **Card 5**: `[Gross Profit Margin %]` (14.23%)
2. **Monthly Net Sales & Profit Trajectory** (Line and Clustered Column, Width=1180, Height=420):
   - X-Axis: `FinancialFact[YearMonth]`
   - Column: `[Net Sales]`
   - Line: `[Total Profit]`
3. **Country Performance Matrix** (Clustered Bar Chart, Width=640, Height=420):
   - Y-Axis: `FinancialFact[Country]`
   - Values: `[Net Sales]`, `[Total Profit]`
4. **Segment Revenue & Profit Contribution** (Donut Chart & Table, Bottom, Width=1840, Height=430):
   - Breakdown across Government, Small Business, Enterprise, Midmarket, and Channel Partners.
   - Highlights the Enterprise operating deficit.

---

## 3. Page 2 — Margin & Cost Analysis

### A. Purpose
Examines managerial cost structures, COGS absorption rates, product line margins, and the income statement bridge.

### B. Visual Layout
1. **Corporate Income Statement Waterfall Bridge** (Top Left, Width=1050, Height=480):
   - Bridge from Gross Sales (\$127.93M) -> Less Discounts (-\$9.21M) -> Net Sales (\$118.73M) -> Less COGS (-\$101.83M) -> Profit (\$16.89M).
2. **COGS Ratio % across Product Lines** (Top Right, Width=770, Height=480):
   - X-Axis: `FinancialFact[Product]`
   - Bar Values: `[COGS Ratio %]`
   - Reference Line: Company-wide COGS ratio ($85.77\%$).
3. **Discount Sensitivity vs. Operating Margin** (Bottom Left, Width=920, Height=460):
   - X-Axis: `FinancialFact[Discount Band]` (None, Low, Medium, High)
   - Y-Axis: `[Gross Profit Margin %]`
4. **Product Profitability Ranking Table** (Bottom Right, Width=900, Height=460):
   - Columns: `Product`, `Units Sold`, `Gross Sales`, `Net Sales`, `COGS`, `Profit`, `Gross Profit Margin %`.

---

## 4. Page 3 — Variance & Scenario Analysis

### A. Purpose
Enables FP&A and CFO teams to interactively simulate the financial impact of commercial discount adjustments and supply chain COGS inflation.

### B. Visual Layout
1. **Interactive What-If Sliders** (Top Left, Width=550, Height=300):
   - **Slider 1**: Discount Adjustment % (`-30%` to `+30%`, Default `0%`).
   - **Slider 2**: COGS Inflation % (`-20%` to `+20%`, Default `0%`).
2. **Baseline vs. Simulated Performance Cards** (Top Right, Width=1270, Height=300):
   - Side-by-side callout cards:
     - Baseline Profit (\$16.89M) vs. Simulated Profit
     - Baseline Margin (14.23%) vs. Simulated Margin %
     - Net Variance Delta (`[Scenario Profit Dollar Variance]`, formatted as green/red currency).
3. **Sensitivity Scenario Tornado Chart** (Bottom Left, Width=920, Height=640):
   - Visualizes operating profit across 6 standardized scenarios (Severe Inflation, Moderate Inflation, Baseline, Discount Discipline, Strict Governance, Optimized).
4. **Dynamic Simulated Statement Table** (Bottom Right, Width=900, Height=640):
   - Statement line items dynamically recalculating based on slider inputs.
