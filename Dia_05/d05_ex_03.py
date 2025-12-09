# 3) Limpeza de dados com .loc
# Crie um DataFrame fictício ou use o seu e faça:
# Trocar todos os nomes contendo "joao" por "João" (corrigindo capitalização).
# Corrigir cidades escritas errado:
# “Sao Paulo” → “São Paulo”
# “Belo horzonte” → “Belo Horizonte”
# Padronizar tudo na coluna cidade para title case (ex.: “rio de janeiro” → “Rio De Janeiro”).
# Use .loc para localizar quem está errado antes de aplicar as correções.

import pandas as pd

df = pd.read_csv('dados_sujos.csv')

df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
df.loc[(df['idade'] < 0) | (df['idade'] > 120), 'idade'] = None
df['idade'] = df['idade'].astype('Int64')

# A partir daqui, exercício 02
df.loc[df['idade'] < 18, 'faixa_idade'] = 'menor'
df.loc[(df['idade'] >= 18) & (df['idade'] < 60), 'faixa_idade'] = 'adulto'
df.loc[df['idade'] >= 60, 'faixa_idade'] = 'idoso'

df['salario'] = (
    df['salario']
    .astype(str)
    .str.strip()
    .str.replace(' ', '', regex=False)
    .str.replace('R$', '', regex=False)
    .str.replace('\.', '', regex=True)
    .str.replace(',', '.', regex=False)
)
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')
df['salario_anual'] = df['salario'] * 12

# A partir daqui, exercício 03
df['nome'] = (
    df['nome']
    .astype(str)
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)
    .str.replace(r'(?<=[A-Za-z])\s+(?=[A-Za-z])', '', regex=True)
)

df.loc[df['nome'].str.contains('joao', case=False, na=False), 'nome'] = 'João'
df.loc[df['nome'].str.contains('Carolos', case=False, na=False), 'nome'] = 'Carlos'
df.loc[df['nome'].str.contains('Brunno', case=False, na=False), 'nome'] = 'Bruno'

df.loc[df['cidade'].str.contains(r'sao paulo|sao|sp', case=False, regex=True), 'cidade'] = 'São Paulo'
df.loc[df['cidade'].str.contains(r'rio de janero|janero|rj', case=False, regex=True), 'cidade'] = 'Rio de Janeiro'
df.loc[df['cidade'].str.contains(r'curitba', case=False, regex=True), 'cidade'] = 'Curitiba'

df['cidade'] = (
    df['cidade']
    .astype(str)
    .str.strip()
    .str.title()
    .str.replace(r'\s+', ' ', regex=True)
)

df['departamento'] = (
    df['departamento']
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)        # normaliza espaços
    .str.replace(r'(?<=\w)\s+(?=\w)', '', regex=True)  # remove espaço indevido dentro da palavra
    .str.title()
)

df.loc[df['departamento'].str.contains(r'\btecnologia\b|\bti\b', case=False, regex=True), 'departamento'] = 'TI'
df.loc[df['departamento'].str.contains(r'\brh\b', case=False, regex=True), 'departamento'] = 'RH'

print(df)
