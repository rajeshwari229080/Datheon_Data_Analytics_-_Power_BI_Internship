# Official LinkedIn Announcement & Portfolio Post

> **Media Asset to Attach**: Attach `docs/assets/linkedin_showcase_light.png` (or a multi-image carousel using `hero_banner_light.png`, `risk_framework_light.png`, and `portfolio_quadrant_light.png`).

---

## LinkedIn Post Text (Copy & Paste Ready)

🚀 Excited to unveil a complete, evidence-driven enterprise analytics solution: the **RISK Master Framework — Enterprise Data Analytics & Business Intelligence Suite**!

Most portfolio dashboards in data analytics stop at superficial charts, synthetic clean data, or disconnected visuals. For this project, I took an enterprise-grade approach, integrating **four commercial analytics projects** across retail merchandising, dimensional modeling, customer retention, and corporate finance using the **RISK Framework**:

🔹 **R — Requirements & Research**  
🔹 **I — Investigation & Insight Discovery**  
🔹 **S — Solution Engineering**  
🔹 **K — Knowledge Delivery & KPI Validation**  

Here is what was built, audited, and mathematically reconciled across 4 real-world datasets:

---

### 📊 1. Retail Sales EDA & Discount Elasticity (Superstore)
• Forensic discovery: unmasked 806 appended metadata rows (`People` and `Returns`) hidden at the bottom of the raw CSV, isolating 9,994 clean orders.  
• Isolated the **20% Discount Cliff**: while discounts between 0% and 10% yielded healthy positive margins (+27.9% and +14.8%), discounts >20% triggered severe profit destruction (-17.9% to -87.8%), eroding **$64,346 in operating profit**.  
• Identified unintended loss leaders: Tables (-$17.7k loss) and Bookcases (-$3.5k loss).  
• Discovered Central territory margin lag (7.9% vs. West's 14.9%) driven by 24.0% average discounting.  

---

### 📐 2. Interactive Power BI Executive Dashboard & Star Schema
• Re-architected flat transactions into a normalized **Kimball Star Schema**: `FactSales` (9,994 lines), continuous calendar `DimDate` (1,826 days from 2014–2018), `DimCustomer`, `DimProduct`, and `DimGeography`.  
• Created production **DAX measures with continuous time-intelligence**: Total Sales ($2,297,201), Total Profit ($286,397), YoY Sales Growth %, Profit Margin %, and Order Return Rate %.  
• Architected a 4-page executive dashboard (Executive Overview, Product Profitability, Customer Dynamics, and Variance Analysis).  
• **Reconciliation Audit**: Proved **$0.00 variance (100% match)** between Python aggregations and Power BI DAX calculations across all dimensions.  

---

### 👥 3. Customer Retention & Cohort Dynamics (IBM Telco)
• Audited 7,043 subscriber accounts; baseline churn of **26.54%** (1,869 accounts), exposing **$139,131 in monthly recurring revenue (MRR)**.  
• Uncovered the **first-year onboarding cliff**: the 0–12 month tenure cohort churns at **47.44%**, accounting for 55.5% of all portfolio attrition.  
• Isolated major churn triggers: month-to-month contracts churn at **42.71%** (15.1x higher risk than 2-year contracts); fiber optic subscribers without tech support churn at **51.81%**; electronic check users churn at **45.29%**.  
• Formulated 3 commercial retention initiatives projected to save **+$251,300 in net annual ARR** (ROI = 297%).  
• Documented critical methodological controls distinguishing cross-sectional survivor distributions from longitudinal panel retention curves.  

---

### 💼 4. Corporate Financial Performance & Margin Sensitivity
• Verified corporate income statement: Gross Sales ($127.93M) ➔ Less Discounts (-$9.21M) ➔ Net Sales ($118.73M) ➔ Less COGS (-$101.83M) ➔ Operating Profit (**$16.89M**, 14.23% margin).  
• **The Enterprise Deficit Discovery**: The Enterprise segment generated $19.61M in net sales but operated at a **-$616,900 net loss** due to a 103.15% COGS absorption ratio!  
• Government segment stood as the company profit engine ($11.39M profit, 21.69% margin, driving 67.4% of total profit).  
• Engineered **Power BI What-If parameter sliders** for Discount adjustments (±30%) and COGS inflation (±20%) with dynamic DAX recalculations.  

---

### 🛠️ Engineering Standards & Quality Assurance
✅ **20 Automated Pytest Tests Passing** (Schema validation, data cleaning assertions, mathematical invariance, and Star-Schema referential integrity).  
✅ **Modular Python Engine**: Ingestion (`src/data_loader.py`), Data Quality (`src/data_validation.py`), Deterministic Cleaning (`src/data_cleaning.py`), and Centralized Metrics (`src/metrics.py`).  
✅ **Pre-Executed Jupyter Notebooks**: All 4 notebooks run head-to-tail with embedded outputs and 17 high-DPI charts.  
✅ **30 Phased Git Commits**: Built incrementally on GitHub following professional commit conventions.  

🔗 **Explore the full codebase, notebooks, and documentation on GitHub**:  
https://github.com/rajeshwari229080/Datheon_Data_Analytics_-_Power_BI_Internship

I'd love to hear your thoughts on discount elasticity governance and dimensional modeling in Power BI! How do your teams handle unintended loss leaders in retail?

#DataAnalytics #BusinessIntelligence #PowerBI #DataScience #Python #DAX #DataModeling #FinancialAnalysis #CustomerRetention #EDA #DataEngineering #Kimball #PortfolioProject
