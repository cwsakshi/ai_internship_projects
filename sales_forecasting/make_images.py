# sales_forecasting/src/make_images.py
# Run from repo root:
#   python sales_forecasting/src/make_images.py

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Define project paths
PROJECT = Path('sales_forecasting')
DATA = PROJECT / 'data' / 'sales_synthetic.csv'   # check filename matches yours
OUT = PROJECT / 'images'
OUT.mkdir(parents=True, exist_ok=True)

# Load dataset
df = pd.read_csv(DATA, parse_dates=['date'])
df = df.sort_values('date')

# 1) Sales trend plot
plt.figure(figsize=(10,4))
plt.plot(df['date'], df['sales'], label='Sales')
plt.title('Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig(OUT / 'sales_trend.png', dpi=150)
plt.close()
print('Saved:', OUT / 'sales_trend.png')

# 2) Simple forecast (7-day rolling average as baseline)
df_daily = df.set_index('date').resample('D').sum().interpolate()
df_daily['rolling7'] = df_daily['sales'].rolling(7, min_periods=1).mean()

last_value = df_daily['rolling7'].iloc[-1]
future_idx = pd.date_range(df_daily.index[-1] + pd.Timedelta(days=1), periods=90, freq='D')
fc = pd.Series(index=future_idx, data=last_value)

plt.figure(figsize=(10,4))
plt.plot(df_daily.index, df_daily['sales'], label='History')
plt.plot(df_daily.index, df_daily['rolling7'], label='Rolling(7)')
plt.plot(fc.index, fc.values, label='Forecast (baseline)', linestyle='--')
plt.legend()
plt.title('Forecast (simple baseline)')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.tight_layout()
plt.savefig(OUT / 'forecast_plot.png', dpi=150)
plt.close()
print('Saved:', OUT / 'forecast_plot.png')
