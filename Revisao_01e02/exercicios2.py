import pandas as pd

df = pd.read_csv('dados.csv')

print(df.head())
df.info()
print(df.describe())
print(df['nome'].head())