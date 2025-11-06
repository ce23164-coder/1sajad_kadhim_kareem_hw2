import pandas as pd


data = {
    "City": ["Baghdad", "Basra", "Erbil", "Mosul", "Najaf"],
    "Temp": [42, 45, 38, 29, 44]
}
df = pd.DataFrame(data)


temps_series = df["Temp"]


above_30 = temps_series[temps_series > 30]


print(above_30)