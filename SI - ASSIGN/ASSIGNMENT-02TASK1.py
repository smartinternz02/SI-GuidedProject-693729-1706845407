import pandas as pd
df = pd.read_csv(r"C:\Users\perur\OneDrive\Desktop\SI GUIDED data set.csv")
print(df.head())
print(df.isnull().sum())
print(df.dtypes)
