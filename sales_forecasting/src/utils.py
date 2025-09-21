# Utility helpers for time series
def add_date_parts(df, date_col='Date'):
    df = df.copy()
    dt = pd.to_datetime(df[date_col])
    df['year'] = dt.dt.year
    df['month'] = dt.dt.month
    df['day'] = dt.dt.day
    df['dow'] = dt.dt.dayofweek
    return df
