import pandas as pd

# load dataset
df = pd.read_csv("makeup_products.csv")

# show first 5 rows
print("First 5 rows:")
print(df.head())

# basic info
print("\nDataset Info:")
print(df.info())

# number of products per brand
print("\nProducts per brand:")
print(df["brand"].value_counts().head())

# average price
print("\nAverage price:")
df["price"] = pd.to_numeric(df["price"], errors="coerce")
print(df["price"].mean())