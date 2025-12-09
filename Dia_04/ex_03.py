# EXERCÍCIO 3 — Alterando valores específicos

import pandas as pd

df = pd.read_csv('dados.csv')

df.loc[df['nome'] == 'João', 'salario'] *= 1.2
print(df)
