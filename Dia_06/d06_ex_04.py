# EXERCÍCIO 04 — Padronização da coluna cargo
# Objetivo:
# Padronizar a coluna cargo usando .loc, criando 3 rótulos:
# - "Analista de Dados"
# - "Cientista de Dados"
# - "Outro"

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

# A partir daqui, exercício 04
df['cargo'] = (
    df['cargo']
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(r'\s+', ' ', regex=True)
)

df.loc[df['cargo'].str.contains(r'analista.*dados', case=False, regex=True), 'cargo'] = 'Analista de Dados'
df.loc[df['cargo'].str.contains(r'cientista.*dados', case=False, regex=True), 'cargo'] = 'Cientista de Dados'
df.loc[~df['cargo'].isin(['Analista de Dados', 'Cientista de Dados']), 'cargo'] = 'Outro'

print(df[['nome', 'cargo']])
