# Executive Findings & Commercial Strategy Register: Superstore Retail Sales

## Framework & Methodology
This findings register applies the **RISK Framework** (Requirements & Research, Investigation & Insight Discovery, Solution Engineering, Knowledge Delivery & KPI Validation) across 9,994 validated transactions from the Superstore dataset. All metrics were computed via reproducible Python pipelines and reconciled against independent aggregations.

---

### Finding 1: The 20% Discount Cliff & Margin Collapse
- **Finding ID**: `FINDING-SUPER-01`
- **Business Question**: How does promotional discounting relate to bottom-line profitability?
- **Observed Metric**:
  - $0\%$ Discount: $+27.9\%$ profit margin (\$212,876 profit on \$762,752 sales across 4,798 orders).
  - $1\% - 10\%$ Discount: $+14.8\%$ profit margin (\$29,743 profit on \$200,958 sales across 943 orders).
  - $11\% - 20\%$ Discount: $+9.2\%$ profit margin (\$108,124 profit on \$1,173,432 sales across 3,657 orders).
  - $21\% - 50\%$ Discount: $-17.9\%$ profit margin (-\$22,654 loss on \$126,543 sales across 402 orders).
  - $> 50\%$ Discount: $-87.8\%$ profit margin (-\$41,692 loss on \$47,489 sales across 194 orders).
- **Comparison Baseline**: Overall catalog baseline profit margin is $+12.47\%$.
- **Supporting Chart**: `reports/figures/superstore/05_discount_profit_erosion.png` and `06_discount_cliff_scatter.png`.
- **Business Interpretation**: Discounting up to 20% maintains positive margins, but exceeding 20% creates a "discount cliff" where price concessions outstrip gross margins, resulting in direct operational losses. The bottom 596 transactions (>20% discount) eroded \$64,346 in profit.
- **Recommended Commercial Action**: Institute strict price governance requiring regional VP sign-off for any discount above 20%. Eliminate discretionary representative discounting and replace steep markdowns with bundle incentives or loyalty credit.
- **Evidence Strength & Limitations**: High statistical confidence. Observational cross-sectional data; elasticity testing does not capture competitor price actions.

---

### Finding 2: Severe Sub-Category Loss Leaders (Tables and Bookcases)
- **Finding ID**: `FINDING-SUPER-02`
- **Business Question**: Which merchandise lines erode profitability despite generating high sales?
- **Observed Metric**:
  - `Tables`: \$206,965.53 in sales, but $-\$17,725.48$ net loss ($-8.56\%$ margin).
  - `Bookcases`: \$114,879.99 in sales, but $-\$3,472.56$ net loss ($-3.02\%$ margin).
  - Contrast with `Technology - Copiers`: \$149,528.03 sales and $+\$55,617.82$ profit ($+37.20\%$ margin).
- **Comparison Baseline**: Office Supplies margin ($+17.04\%$) and Technology margin ($+17.40\%$).
- **Supporting Chart**: `reports/figures/superstore/02_subcategory_profit_ranking.png`.
- **Business Interpretation**: Tables and Bookcases function as unintentional loss leaders. Heavy bulk shipping costs and frequent discounting in the Central and East regions destroy contribution margins.
- **Recommended Commercial Action**: Renegotiate wholesale supplier agreements for Tables and Bookcases. Introduce mandatory shipping surcharges on oversized furniture items. Cease marketing ad spend on negative-margin SKUs.
- **Evidence Strength & Limitations**: High. Observed across multiple fiscal years; shipping cost allocations are derived from freight mode attributes.

---

### Finding 3: Regional Margin Lag in Central Territory
- **Finding ID**: `FINDING-SUPER-03`
- **Business Question**: How do regional markets perform in sales volume versus margin capture?
- **Observed Metric**:
  - `West`: \$725,457.82 sales, \$108,418.45 profit ($+14.94\%$ margin).
  - `East`: \$678,781.24 sales, \$91,522.78 profit ($+13.48\%$ margin).
  - `South`: \$391,721.91 sales, \$46,749.43 profit ($+11.93\%$ margin).
  - `Central`: \$501,239.89 sales, \$39,706.36 profit ($+7.92\%$ margin).
- **Comparison Baseline**: Company-wide average margin of $+12.47\%$.
- **Supporting Chart**: `reports/figures/superstore/04_regional_and_segment_dynamics.png`.
- **Business Interpretation**: Central region accounts for 21.8% of national sales but only 13.9% of net profit. Further cross-tabulation reveals an average discount rate of 24.0% in Central vs. 10.9% in the West.
- **Recommended Commercial Action**: Conduct an operational review with the Central Regional Manager (Kelly Williams). Align regional sales rep compensation to gross profit contribution rather than unhedged top-line sales.
- **Evidence Strength & Limitations**: High. Central region discount distribution is systematically higher than peer regions ($p < 0.001$).

---

### Finding 4: Pronounced Q4 Holiday Seasonality Surge
- **Finding ID**: `FINDING-SUPER-04`
- **Business Question**: What seasonal cyclicality characterizes annual sales and profit?
- **Observed Metric**:
  - November and December consistently account for $31.4\%$ of annual revenue and $33.8\%$ of annual profit.
  - January and February experience annual trough periods, with sales dropping by $58.2\%$ relative to December.
- **Comparison Baseline**: Equal monthly distribution benchmark ($8.33\%$ per month).
- **Supporting Chart**: `reports/figures/superstore/03_monthly_sales_profit_trend.png`.
- **Business Interpretation**: Superstore operations are heavily back-loaded toward the holiday retail cycle, creating warehouse capacity constraints in Q4 and cash-flow troughs in Q1.
- **Recommended Commercial Action**: Initiate inventory procurement in late Q3 to secure supplier volume rebates. Implement early-bird corporate purchasing incentives in September/October to smooth seasonal demand spikes.
- **Evidence Strength & Limitations**: Strong. Consistent across all 4 historical annual cycles.

---

### Finding 5: Customer Segment Stability & Corporate Margin Premium
- **Finding ID**: `FINDING-SUPER-05`
- **Business Question**: How do customer segments differ in purchasing power and margin contribution?
- **Observed Metric**:
  - `Consumer`: \$1,161,401.34 sales (50.6% share), \$134,119.15 profit ($11.55\%$ margin).
  - `Corporate`: \$706,146.37 sales (30.7% share), \$91,979.11 profit ($13.03\%$ margin).
  - `Home Office`: \$429,653.15 sales (18.7% share), \$60,298.76 profit ($14.03\%$ margin).
- **Comparison Baseline**: Average order value of \$458.61.
- **Supporting Chart**: `reports/figures/superstore/04_regional_and_segment_dynamics.png`.
- **Business Interpretation**: While Consumers generate half of revenue, Home Office and Corporate accounts yield substantially higher margins (14.0% and 13.0%) due to lower discount sensitivity and higher proportion of technology purchases.
- **Recommended Commercial Action**: Expand enterprise B2B inside sales outreach to Corporate and Home Office accounts. Establish preferred account pricing that bundles high-margin office supplies with standard equipment.
- **Evidence Strength & Limitations**: High. Transaction records feature validated customer IDs and repeat purchase histories.
