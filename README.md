# Tailwind Traders Executive BI Dashboard 

This repository showcases a complete data-driven business intelligence solution for **Tailwind Traders**, built using Microsoft Power BI and Python. The goal was to transform raw sales and financial data into actionable insights for executive decision-making.

---

##  Business Objective

Tailwind Traders required:
- Global analysis of **sales**, **profits**, and **returns**
- Currency normalization and country-wise performance
- Temporal insights: **Yearly**, **Quarterly**, **YTD**
- Automated dashboards with **subscriptions**, **mobile layout**, and **alerts**

---

## Key Case Studies & Implementations

---

### 1. **Sales Data Report**

- Imported structured `.xlsx` dataset into Power BI
- Cleaned and validated data using Power Query
- Calculated:
  - **Gross Revenue** = \$11,318
  - **Net Revenue** = \$12,137
  - **Tax Impact (Delta)** = \$819
- Ensured column profiling, histogram analysis, and type assignment

📷 *Visual*  
![Sales Report](assets/sales_report.png)

---

### 2. **Data Preparation & Exchange Rate Transformation**

- Prepared and optimized the following:
  - Purchases table
  - Countries + Exchange Rate mapping
- Used **Python script** in Power BI to parse and structure currency data:

```python
import pandas as pd
from io import StringIO

data = """Exchange ID;ExchangeRate;Exchange Currency
1;1;USD
2;0.75;GBP
3;0.85;EUR
4;3.67;AED
5;1.3;AUD"""

df = pd.read_csv(StringIO(data), sep=';')
df
```
---
