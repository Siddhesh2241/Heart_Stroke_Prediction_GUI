import pandas as pd

data = pd.read_csv("heart.csv")

print(data.head())
print(data.dtypes)
print(data.info())
print(data.shape())
print(data.describe())
print(data.isnull().sum())
print(data.isnull().sum())

