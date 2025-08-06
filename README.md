# 🛒 Tailwind Traders: Executive Sales & Profit Dashboard 

This project showcases an end-to-end business intelligence solution for **Tailwind Traders**, built using Microsoft Power BI. It replicates the kind of data challenges faced by real-world organizations and demonstrates how to address them through data transformation, model design, advanced DAX, and dashboarding — aligned with the **Meesho Data Scientist – I** job description.

---

##  Business Objective

Tailwind Traders required a set of strategic dashboards to:

- Analyze global **sales**, **profits**, and **returns** across regions and products
- Enable **data-driven decisions** for revenue growth and cost control
- Provide executives with **mobile-ready performance summaries**
- Deliver **automated alerts and insights** for ongoing monitoring

---

##  Tech Stack

| Tool          | Purpose                                      |
|---------------|----------------------------------------------|
| **Power BI**  | Core data modeling, DAX measures, dashboarding |
| **Python (pandas)** | Data parsing for historical currency rates |
| **DAX**       | Time-based calculations (YTD, QTD, MEDIAN)   |
| **Excel**     | Source dataset preparation                   |

---

##  Features & Deliverables

###  Case Study Implementations:

   ### 1. **Sales Data Report**
- Loaded structured `.xlsx` file into Power BI
- Calculated:
  - **Gross Revenue** = \$11,318
  - **Net Revenue** = \$12,137
  - **Delta (Tax impact)** = Net – Gross = \$819
    
- Used Power Query to ensure column quality, data types, and validation
- Prepared for further aggregation in unified USD model

---

   ### 2. **Data Preparation & Optimization**
- Ensured accurate data types for:
  - Purchase table (Date, Quantity, Price)
  - Countries table (Currency, Country ID)
- Merged and validated exchange rates with country info
- Used the following **Python script** in Power BI to reshape and clean the currency exchange dataset:

```python
import pandas as pd
from io import StringIO

# Simulated historical exchange rate string data (multi-line format)
data = '''Date,USD,EUR,GBP,JPY
2023-01-01,1.0,0.93,0.81,131.2
2023-01-02,1.0,0.94,0.82,130.5
'''

# Read into DataFrame
df = pd.read_csv(StringIO(data), parse_dates=["Date"])

# Output cleaned data
print(df_long.head())
```

---

### 3. **Currency Normalization and Star Schema Modeling**

- Developed a clean **data model** with optimized relationships using **star schema**
- Created the following tables in Power BI:

####  Fact Tables
- `Sales` – core transaction table with gross/net/tax details
- `Sales in USD` – currency-normalized version using DAX logic and country joins

####  Dimension Tables
- `CalendarTable` – auto-generated using DAX for time intelligence
- `Countries` – maps countries to their respective currencies and exchange rates
- `Exchange Data` – historical exchange rate mapping table
- `Purchases` – linked purchase behavior, warranty, and return status

- Ensured proper **1-to-many** cardinality and active joins for clean visual interaction
- Used these joins to drive DAX-based time-series insights, regional aggregations, and executive dashboard views

####  Data Model Snapshot

![Data Model](assets/s3.png)

---

4. **Profitability Insights**
   - Calculated:
     - Yearly Profit Margin
     - Quarterly Profit
     - YTD Profit
     - Median Sales
   - Leveraged `DATESQTD()` and `TOTALYTD()` DAX functions
---
5. **Executive Dashboard**
   - Dual-page report: *Sales Overview* + *Profit Overview*
   - Created `CalendarTable` for time intelligence
   - Added card visuals, pie/bar/line charts
   - Pinned to **mobile-optimized dashboard**
---
6. **Monitoring Tools**
   - Setup **Power BI Subscriptions** for weekly profit/sales reports
   - Used **Performance Analyzer** to optimize visuals

---
---
## Visual Snapshots

> _Screenshots from actual Power BI implementation are available in the `/assets` folder._

| Sales Overview | Profit Overview |
|----------------|------------------|
| ![Sales](assets/sales_overview.png) | ![Profit](assets/profit_overview.png) |

---
---
## 📂 Folder Structure

