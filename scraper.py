import requests
import pandas as pd

url = "https://makeup-api.herokuapp.com/api/v1/products.json"

response = requests.get(url)
data = response.json()

# Convert to dataframe
df = pd.DataFrame(data)

# Keep only useful columns
df = df[["brand","name","price","rating","category","product_type"]]

# Save dataset
df.to_csv("makeup_products.csv", index=False)

print("Dataset saved successfully!")
