import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

# Load files
sales = pd.read_excel('_Tailwind-Traders-Sales.xlsx')
countries = pd.read_excel('Countries.xlsx')

# Currency exchange
from io import StringIO
data = """Exchange ID;ExchangeRate;Exchange Currency
1;1;USD
2;0.75;GBP
3;0.85;EUR
4;3.67;AED
5;1.3;AUD"""
exchange_df = pd.read_csv(StringIO(data), sep=';')

# Merge
countries_merged = countries.merge(exchange_df, on="Exchange ID", how="left")
sales = sales.merge(countries_merged, left_on=" Country ID", right_on="Country ID", how="left")

# Revenue calculation
sales["Net Revenue"] = sales["Gross Product Price"] * sales["Quantity Purchased"]
sales["Gross Revenue"] = sales["Net Revenue"] + sales["Tax Per Product"] * sales["Quantity Purchased"]
sales["Gross Revenue USD"] = sales["Gross Revenue"] * sales["ExchangeRate"]
sales["Time Index"] = sales.index

# Features and target
X = sales[[
    "Gross Product Price", "Tax Per Product", "Quantity Purchased",
    "ExchangeRate", "Net Revenue", "Gross Revenue", "Time Index"
]]
y = sales["Gross Revenue USD"]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = XGBRegressor(n_estimators=80, max_depth=4, learning_rate=0.1, subsample=0.8, colsample_bytree=0.8, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Evaluate
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("R² Score:", round(r2, 4))
print("MSE:", round(mse, 2))

# Plot feature importance
model.get_booster().feature_names = X.columns.tolist()
XGBRegressor().get_booster()
model.get_booster().feature_names = X.columns.tolist()
model.get_booster().feature_names = X.columns.tolist()
model.get_booster().feature_names = X.columns.tolist()
model.get_booster().feature_names = X.columns.tolist()
model.get_booster().feature_names = X.columns.tolist()
model.get_booster().feature_names = X.columns.tolist()
model.get_booster().feature_names = X.columns.tolist()
model.get_booster().feature_names = X.columns.tolist()

# Plot Actual vs Predicted Gross Revenue USD
plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred, alpha=0.6, color='teal', edgecolors='k')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel("Actual Revenue (USD)")
plt.ylabel("Predicted Revenue (USD)")
plt.title("Actual vs Predicted Gross Revenue")
plt.grid(True)
plt.tight_layout()
plt.show()



