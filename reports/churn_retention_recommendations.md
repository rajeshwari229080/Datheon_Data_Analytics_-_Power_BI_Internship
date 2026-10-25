# Customer Retention Playbook & Churn Risk Analysis: IBM Telco

## 1. Executive Summary
This analysis evaluates subscriber retention, cross-sectional cohort survival patterns, and structural attrition risks across 7,043 customer accounts in the IBM Telco portfolio.

### Portfolio Retention Overview:
- **Total Customer Accounts**: 7,043
- **Retained Customer Accounts**: 5,174 ($73.46\%$)
- **Churned Customer Accounts**: 1,869 ($26.54\%$)
- **Total Monthly Recurring Revenue (MRR)**: \$456,116.60
- **Monthly Revenue Lost to Churn**: \$139,130.85 ($30.50\%$ of monthly cash flow)
- **Annualized Revenue Exposure (ARR Loss)**: **\$1,669,570.20**

---

## 2. Evidence-Supported Quantified Findings

### Finding 1: The Month-to-Month Contract Vulnerability
- **Empirical Metric**: Month-to-month subscribers experience an attrition rate of **$42.71\%$** (1,655 churned out of 3,875 subscribers).
- **Comparison Baseline**: One-year contract churn is **$11.27\%$** (166 / 1,473), and Two-year contract churn is **$2.83\%$** (48 / 1,695).
- **Relative Risk Ratio**: Month-to-month subscribers are **$15.1\times$** more likely to churn than Two-year contract holders.
- **Root Cause Interpretation**: Month-to-month agreements impose zero switching friction. Customers churn opportunistically upon receiving promotional marketing from rival carriers or encountering minor billing disputes.

### Finding 2: High Attrition in Early Lifecycle (Tenure 0–12 Months)
- **Empirical Metric**: The 0–12 month tenure cohort exhibits a **$47.44\%$** churn rate (1,037 accounts lost out of 2,186 total cohort accounts).
- **Comparison Baseline**: Accounts surviving past 24 months drop below $20\%$ churn, and accounts past 48 months drop to $10.1\%$, reaching $6.6\%$ in months 61–72.
- **Concentration**: Over **$55.5\%$** of all portfolio churn occurs during the first 12 months of service.
- **Root Cause Interpretation**: The first year represents the "onboarding cliff"—dissatisfaction with installation, initial bill transparency, or broadband speed variance causes acute early drop-off.

### Finding 3: The Fiber Optic Technical Support Deficit
- **Empirical Metric**: Fiber optic subscribers lacking technical support experience an extreme churn rate of **$51.81\%$** (802 churned out of 1,548 customers).
- **Comparison Baseline**: Fiber optic subscribers with dedicated technical support experience a substantially lower churn rate of **$27.60\%$** (228 / 826). DSL subscribers without tech support churn at $39.5\%$.
- **Revenue Exposure**: Fiber optic accounts carry the highest average monthly charges (\$91.50/month). Unresolved technical friction directly imperils the most lucrative subscriber cohort.

### Finding 4: Electronic Check Payment Channel Friction
- **Empirical Metric**: Customers paying via manual Electronic Check churn at **$45.29\%$** (1,071 churned out of 2,365 customers).
- **Comparison Baseline**: Customers enrolled in automated Bank Transfer churn at **$16.71\%$** (258 / 1,544), and Credit Card auto-pay churns at **$15.24\%$** (232 / 1,522).
- **Root Cause Interpretation**: Electronic Check requires active monthly intervention and conscious payment appraisal. Automated payment methods decouple monthly service utility from transactional scrutiny.

### Finding 5: Higher Bill Value Sensitivity
- **Empirical Metric**: Churned customers exhibit an average monthly charge of **\$74.44**, compared to **\$61.27** for retained customers (difference $= +\$13.17$, $t = 16.54$, $p < 0.001$).
- **Distribution**: Peak churn occurs within the \$70–\$105/month band, driven primarily by fiber optic and multi-line bundles.

---

## 3. Prioritized High-Risk Customer Segments

| Priority Tier | Multi-Attribute Segment Profile | Active Base | Churn Rate % | Monthly Revenue at Risk | Primary Risk Factor |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1 (Extreme)** | Month-to-month + Fiber Optic + No Tech Support | 1,548 | **51.8%** | \$73,380.00 | Technical friction + lack of commitment |
| **Tier 2 (High)** | Month-to-month + Electronic Check | 2,365 | **45.3%** | \$48,210.00 | Manual bill friction + no lock-in |
| **Tier 3 (High)** | Tenure 0–12m + Fiber Optic | 1,024 | **44.9%** | \$38,950.00 | Early lifecycle dissatisfaction |
| **Tier 4 (Moderate)**| Month-to-month + DSL + No Online Security | 872 | **35.1%** | \$14,620.00 | Perceived value deficit |

---

## 4. Actionable Retention Initiatives & Financial ROI

### Initiative 1: The "Stay & Save" Contract Migration Engine
- **Target Population**: Month-to-month subscribers with 4–8 months of tenure (approx. 1,400 accounts).
- **Mechanism**: Push an automated in-app/SMS offer providing a \$10/month bill credit for 3 months upon committing to a 12-month agreement.
- **Projected Impact**: Converting 25% of target accounts (350 subscribers) from month-to-month ($42.7\%$ churn) to 1-year contract ($11.3\%$ churn) preserves approximately 110 customers annually, saving **\$105,600 ARR**.

### Initiative 2: Auto-Pay Transition Rebate Program
- **Target Population**: 2,365 customers currently paying via Electronic Check.
- **Mechanism**: Offer a recurring \$2.50 monthly statement discount for enrolling in recurring ACH or Credit Card auto-pay.
- **Projected Impact**: Transitioning 30% of electronic check users (710 accounts) to auto-pay is estimated to reduce segment churn by 12 percentage points, preserving 85 subscribers and generating **\$76,500 net annual retention value**.

### Initiative 3: Complimentary 90-Day "Fiber Care" Support Bundle
- **Target Population**: All new Fiber Optic activations.
- **Mechanism**: Automatically bundle 24/7 Priority Tech Support and Cybersecurity Protection for the first 90 days at zero additional charge, followed by a discounted \$5/month opt-in.
- **Projected Impact**: Mitigates early setup friction and targets the 51.8% fiber churn rate, saving an estimated 140 premium subscribers annually (**\$153,700 ARR**).

### Financial Summary of Initiatives:
- **Total Annual Cost of Incentives**: \$84,500
- **Total Gross Revenue Saved**: \$335,800
- **Net Annual Portfolio Benefit**: **+\$251,300 ARR** (ROI = $297\%$)
