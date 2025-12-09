# EXERCÍCIO 4 — Atualização condicional

import pandas as pd

df = pd.read_csv('dados.csv')

df.loc[df['salario'] < 2500, 'salario'] += 300
print(df)
