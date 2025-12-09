# EXERCÍCIO 3 — Padronizar salário e transformar em número
# Objetivo:
# Pegar a coluna salario, que está TODA bagunçada, e:
# - limpar,
# - padronizar,
# - transformar em número (float),
# - e criar uma nova coluna com o salário anual.

import pandas as pd

df = pd.read_csv('dados.csv')

# Exercício 02
df['cidade'] = (
    df['cidade']
    .astype(str)
    .str.strip()
    .str.lower()
    .str.title()
)

df.loc[df['cidade'].str.contains(r'sao paulo|sampa|sp', case=False, regex=True), 'cidade'] = 'São Paulo'
df.loc[df['cidade'].str.contains(r'rio de janeiro|rio|rj', case=False, regex=True), 'cidade'] = 'Rio de Janeiro'

print(df[df['cidade'] == 'São Paulo'])

# A partir daqui, exercício 03
print(df[df['salario'].str.contains(r'[.,]')])

df['salario'] = (
    df['salario']
    .astype(str)
    .str.replace('.', '', regex=False)
    .str.replace(',', '', regex=False)
    .astype(float)
)

df.loc[:, 'salario_anual'] = df['salario'] * 12

print(df[['nome', 'salario', 'salario_anual']])
