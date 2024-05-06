import pandas as pd

# Read the original CSV file
df = pd.read_csv('archive\\orders.csv')

# Convert 'order_date' to datetime format
df['order_date'] = pd.to_datetime(df['order_date'])
df['shipped_date'] = pd.to_datetime(df['shipped_date'])

# Extract day, month, year, and quarter for order_date
df['ORDER_DAY'] = df['order_date'].dt.day
df['ORDER_MONTH'] = df['order_date'].dt.month
df['ORDER_YEAR'] = df['order_date'].dt.year
df['ORDER_QUARTER'] = df['order_date'].dt.quarter

# Extract day, month, year, and quarter for shipped_date
df['SHIPPED_DAY'] = df['shipped_date'].dt.day
df['SHIPPED_MONTH'] = df['shipped_date'].dt.month
df['SHIPPED_YEAR'] = df['shipped_date'].dt.year
df['SHIPPED_QUARTER'] = df['shipped_date'].dt.quarter

# Format the date components
df['ORDER_DAY_MONTH'] = df['order_date'].dt.strftime('%d-%m')
df['SHIPPED_DAY_MONTH'] = df['shipped_date'].dt.strftime('%d-%m')

# Save to a new CSV file named 'date.csv'
df[['order_date', 'ORDER_DAY_MONTH', 'ORDER_MONTH', 'ORDER_YEAR', 'ORDER_QUARTER']].to_csv('date.csv', index=False)
