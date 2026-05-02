import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("makeup_products.csv")

# Top 5 brands chart
top_brands = df["brand"].value_counts().head(5)

plt.figure()
top_brands.plot(kind="bar")
plt.title("Top 5 Makeup Brands by Number of Products")
plt.xlabel("Brand")
plt.ylabel("Number of Products")
plt.show()

# Price distribution chart
plt.figure()
df["price"].dropna().plot(kind="hist", bins=20)
plt.title("Price Distribution of Products")
plt.xlabel("Price")
plt.ylabel("Count")
plt.show()