# EXERCÍCIO 1 — Seleção simples com .loc
# Crie um filtro usando .loc para selecionar apenas nome e salário das pessoas com idade maior que 30.

import pandas as pd

df = pd.read_csv('dados.csv')

filtro = df.loc[df['idade'] > 30, ['nome', 'salario']].sort_values('salario', ascending=False)
print(filtro)
