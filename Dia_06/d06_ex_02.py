# EXERCÍCIO 2 — Padronização de cidades com .loc + str.contains
# Objetivo:
# Padronizar todas as variações de “São Paulo” dentro da coluna cidade.

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
