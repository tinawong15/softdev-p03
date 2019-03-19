import os
import pandas as pd

print("----- Series -----")
your_series = pd.Series([1,2,3,4])
print(your_series)

print("----- Create a DataFrame -----")
df = pd.DataFrame({
    "Integers": [1, 23, 456, 7890],
    "Strings": ['hello', 'pandas', 'world', '!'],
    "Floats": [1.23, 23.5, 45.6, 7.890],
    "Booleans": [True, False, True, False]
})
print(df)
print(df["Strings"])
print(df["Integers"].mean())
print(df.max())


print("----- Get a Column of a DataFrame -----")
print(df["Integers"])

print("----- Create a DataFrame with Existing List -----")
your_list = [4, 8, 12, 16, 20]
df = pd.DataFrame(your_list)
print(df)

print("----- Create a DataFrame with Existing csv -----")
csv_path = 'cities.csv'
print(csv_path)
df = pd.read_csv(csv_path, delimiter=",")
print(df)
print(df.tail())
print(df.sample(3))
print(df.iloc[0:4,:])


