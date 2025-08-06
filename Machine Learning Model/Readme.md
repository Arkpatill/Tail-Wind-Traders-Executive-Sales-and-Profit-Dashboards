# Revenue Prediction Model (XGBoost)

This module implements a machine learning pipeline using **XGBoost Regression** to predict **Gross Revenue (USD)** from retail sales data. It is part of the broader business intelligence and analytics system under this repository.

---

##  Objective

To build a high-accuracy regression model that:
- Predicts gross revenue for transactions using normalized values
- Incorporates country-wise currency conversion
- Achieves high R² performance (≈ 0.84) with real-world retail features

---

##  Files Included

| File                                | Description                                      |
|-------------------------------------|--------------------------------------------------|
| `revenue_prediction_XG Boost.py`   | Core ML pipeline and model logic (XGBoost)       |
| `_Tailwind-Traders-Sales.xlsx`     | Raw transaction-level sales data                 |
| `Countries.xlsx`                   | Country metadata including currency mapping      |

---

##  Technologies Used

- Python 3.11+
- XGBoost
- Scikit-Learn
- Pandas
- Matplotlib

---

##  Installation (if running locally)

1. Clone this repository or download the `ml_model/` folder
2. Install dependencies:

```bash
pip install xgboost scikit-learn pandas matplotlib openpyxl
 How to Run
Ensure the Excel files (_Tailwind-Traders-Sales.xlsx, Countries.xlsx) are in the same directory as the Python script.

Run the model:

bash

python "revenue_prediction_XG Boost.py"
```
### Model Output:

After running, you'll see the model's performance metrics:

<img src="https://github.com/YOUR_USERNAME/YOUR_REPO/blob/main/ml_model/accuracy%20value%20.png?raw=true" width="700"/>
Metric	Value
R² Score	0.8438
MSE	10861.32
RMSE	≈ 104 USD

RMSE is the average deviation between predicted and actual revenue values.
```
---

### Model Features
The model uses the following predictors:
```
Gross Product Price

Tax Per Product

Quantity Purchased

ExchangeRate

Net Revenue

Gross Revenue

Time Index
```
These features are engineered from raw sales and currency data for better prediction accuracy.

---

### Results Snapshot
Metric	Value
R² Score	≈ 0.84
MSE	≈ 10,816
RMSE (Error)	≈ ±104 USD


### Use Cases
This model supports:
```
1. Sales forecasting

2. Revenue analytics

3. Decision dashboards

4. Financial anomaly detection
```
