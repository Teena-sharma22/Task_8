import pandas as pd
import numpy as np

# load dataset
data = pd.read_csv("SuperMarket Analysis.csv")
print("top 5:",data.head())
print("last 5:",data.tail())

print("information:",data.info())
print("description:",data.describe())

# cleaning for visualization
data = data.drop(columns=['gross margin percentage', 'Rating', 'Payment', 'cogs'])

# Format as 'Month-Year' (e.g., Jan-2024)
data['Date'] = pd.to_datetime(data['Date'])

data['Order Month'] = data['Date'].dt.strftime('%b-%Y')

#saving clean data
data.to_csv('clean_data.csv', index=False)
