# Methodological Controls, Limitations & Causality Disclaimers

## Framework & Scientific Integrity
In alignment with the **RISK Framework** (Knowledge Delivery & KPI Validation) and reproducible data science standards, this document establishes clear methodological boundaries, assumptions, and causality constraints across all four analytics projects.

---

## 1. Customer Churn & Cohort Analytics Limitations (IBM Telco)

### A. Cross-Sectional Snapshot vs. True Longitudinal Panel Retention
- **Methodological Distinction**: The Telco dataset represents a **single cross-sectional observation window** (a cross-section of subscribers active or churned in a single snapshot).
- **Survival Bias Warning**: While we categorize subscribers into 12-month tenure buckets (e.g., 0–12m, 13–24m, ..., 61–72m), this does **not** represent a true longitudinal cohort followed from Day 0 through Year 5.
- **Confounding Cohort Effects**: Customers with 60+ months of tenure represent a selected, highly loyal survivor population (survivorship bias). Newer customers in the 0–12 month bucket may have been acquired under different marketing channels, onboarding terms, or pricing plans.
- **Analytical Guardrail**: Tenure-based retention curves must be interpreted strictly as *cross-sectional tenure distributions*, not as deterministic multi-year survival probabilities.

### B. Correlation vs. Causation Guardrails
- **Electronic Check Correlation**: Customers paying by Electronic Check exhibit a 45.3% churn rate. This **does not prove** that paying by check causes churn. Rather, Electronic Check is strongly correlated with month-to-month contracts, lack of credit access, and lower engagement. Forcing customers onto auto-pay without incentive could trigger churn rather than prevent it.
- **Fiber Optic & Tech Support**: While Fiber Optic accounts without Tech Support churn at 51.8%, technical support absence may be a proxy for general customer tech-savviness or unaddressed broadband deployment outages in specific geographic nodes.

### C. Predictive Benchmark Generalization
- **Model Role**: The Logistic Regression baseline is intended purely as a linear benchmark on held-out test data (Stratified 80/20 split; Test ROC-AUC = 0.84, Precision = 0.51, Recall = 0.79, F1 = 0.62).
- **Generalization Boundary**: The model parameters reflect historical pricing and market conditions. These relationships may not generalize if competitors introduce new unlimited packages or if macroeconomic inflation alters subscriber willingness to pay.

---

## 2. Retail Sales & Merchandising EDA Limitations (Superstore)

### A. Observational Pricing Data & Missing Cost Structure
- **Gross Profit vs. Contribution Margin**: The Superstore dataset provides `Sales` and `Profit`, from which unit acquisition cost can be deduced. However, it omits **Customer Acquisition Cost (CAC)**, variable warehouse labor, and return shipping costs.
- **Price Elasticity Limitation**: Observed discount rates reflect historical sales representative discretion rather than controlled randomized pricing experiments. Consequently, the observed "discount cliff" reflects both price elasticity and adverse selection (sales reps discounting heavily on difficult-to-sell or obsolete inventory).

### B. Geographic Grain
- While destination City, State, Region, and Postal Code are captured, customer billing address and physical distribution center locations are absent, preventing exact route-mileage freight cost calculations.

---

## 3. Power BI Star Schema Modeling Assumptions

### A. Dimension Surrogate Keys
- Product catalog definitions exhibit minor descriptive variances across time in the source CSV. Dimensions were deduplicated by selecting the latest canonical product title per `Product ID` to enforce strict 1-to-many dimensional cardinalities.
- A synthetic continuous date dimension spanning 1,826 days was generated to power DAX time-intelligence functions, as native DAX time series functions require continuous calendar integrity without skipped dates.

---

## 4. Corporate Financial Performance Limitations (Financial Sample)

### A. Statement Completeness
- The Financial Sample dataset models a single operational income statement table (Gross Sales → Discounts → Net Sales → COGS → Profit).
- It omits balance sheet accounts (Working Capital, Accounts Receivable, Inventory Assets) and cash flow statements. Profit metrics represent gross operational profit, not Net Income after Tax or EBITDA.

### B. Scenario Simulation Boundaries
- The What-If scenario simulations assume linear pass-through of discount cuts and cost inflation. They do not simulate secondary demand elasticity effects (e.g., volume contraction resulting from price increases).
