# EXERCÍCIO 5 — Seleção dupla de linhas e colunas

import pandas as pd

df = pd.read_csv('dados.csv')

filtro = df.loc[(df['idade'] >= 25) & (df['idade'] <= 40), ['nome', 'idade']]
filtro = filtro.sort_values('idade')
print(filtro)
