import pandas as pd


data = {
    "Name": ["Laptop", "Phone", "Screen"],
    "Price": [1000, 700, 300],
    "Quantity": [5, 10, 8]
}
df = pd.DataFrame(data)
print("--- Original DataFrame ---")
print(df)


df["Total Value"] = df["Price"] * df["Quantity"]
print("\n--- After Adding 'Total Value' Column ---")
print(df)


df_sorted = df.sort_values("Total Value", ascending=False)
print("\n--- After Sorting by 'Total Value' ---")
print(df_sorted)


df_sorted.to_csv("products.csv", index=False)
print("\n* Successfully saved to products.csv")

df_new = pd.read_csv("products.csv")
print("\n--- Reading back from products.csv ---")
print(df_new)