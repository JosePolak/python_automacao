# Exercício 2 — Corrigir erros de cidade
# 1. Padronizar a coluna cidade, corrigindo tudo para:
# - "São Paulo"
# - "Rio de Janeiro"
# - "Belo Horizonte"
# 2. Corrigir variações como:
# - “sao paulo”, “Sampa”, “sao”, “sp”, “sp/zone”
# - “rio”, “rj”
# - “bh”, “bele horizonte”, “belho hor.”
# 3. Criar df_cidade_corrigida.

import pandas as pd

df = pd.read_csv('dados_ex08.csv')

df['cidade'] = (
    df['cidade']
    .astype(str)
    .str.strip()
    .str.lower()
)

df.loc[df['cidade'].str.contains(r'sao.*|sp|sampa', case=False, regex=True), 'df_cidade_corrigida'] = 'São Paulo'
df.loc[df['cidade'].str.contains(r'rio.*ro|rj|rio', case=False, regex=True), 'df_cidade_corrigida'] = 'Rio de Janeiro'
df.loc[df['cidade'].str.contains(r'bel.*|bh', case=False, regex=True), 'df_cidade_corrigida'] = 'Belo Horizonte'

print(df)
