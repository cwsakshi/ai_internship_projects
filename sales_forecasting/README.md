# Sales Forecasting

**Goal:** Predict future sales from historical time series data and visualize forecast vs. actual.

## Dataset
- Synthetic daily series: `data/sales_synthetic.csv` (Date, Sales, Promo, Holiday).
- Replace with your real data later (ensure a `Date` and `Sales` column).

## How to Run
1. Open `notebooks/01_data_prep_and_eda.ipynb` to explore trends, seasonality.
2. Run `notebooks/02_modeling_and_forecast.ipynb` to fit SARIMAX and forecast.
3. Export forecast and compare vs actual.

## Models
- SARIMAX (from `statsmodels`) — reliable & simple.
- (Optional) Prophet — add if installed.

## Metrics
- RMSE, MAE, MAPE

## Publish Checklist
- [ ] Plot original series with trend/seasonality highlights
- [ ] Forecast vs. actual plot
- [ ] Error metrics table
- [ ] Brief business insights
