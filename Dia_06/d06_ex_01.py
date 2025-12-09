# EXERCÍCIO 1 — bônus com .notna()
# Objetivo:
# Criar uma coluna baseada na existência ou ausência do valor em outra coluna.

import pandas as pd

df = pd.read_csv('dados_ex01.csv')

df.loc[df['bonus'].notna(), 'status_bonus'] = 'Tem bônus'
df.loc[df['bonus'].isna(), 'status_bonus'] = 'Sem bônus'

print(df)
