# EXERCÍCIO 05 — FILTRAR + CORRIGIR + CRIAR COLUNA (nível médio)
# Usar .loc, filtros combinados e criação de coluna com base em condições.
# Objetivo
    # Treinar:
        # - Combinação de filtros com &
        # - .str.contains() com regex
        # - Atualização de valores usando .loc[condição, coluna] = valor
        # - Criação de colunas condicionais
        # - Construção de dataframes derivados

import pandas as pd

df = pd.read_csv('dados_ex05.csv')

df['cidade'] = (
    df['cidade']
    .astype(str)
    .str.strip()
    .str.lower()
    .str.title()
)

df.loc[df['cidade'].str.contains(r's.*paulo|sampa|sp', case=False, regex=True), 'cidade'] = 'São Paulo'
df.loc[df['cidade'].str.contains(r'Rio De Janeiro', case=False, regex=True), 'cidade'] = 'Rio de Janeiro'

df['cargo'] = (
    df['cargo']
    .astype(str)
    .str.strip()
    .str.lower()
    .str.title()
)

df.loc[df['cargo'].str.contains(r'analista.*dos', case=False, regex=True), 'cargo'] = 'Analista de Dados'
df.loc[df['cargo'].str.contains(r'cientista.*dos', case=False, regex=True), 'cargo'] = 'Cientista de Dados'

ad_sp_menos4000 = df.loc[(df['cargo'] == 'Analista de Dados') & (df['salario'] < 4000) & (df['cidade'] == 'São Paulo'), ['nome', 'cargo', 'cidade', 'salario']]

df.loc[df['salario'] < 3000, 'faixa_salarial'] = 'Baixo'
df.loc[(df['salario'] >= 3000) & (df['salario'] < 6000), 'faixa_salarial'] = 'Médio'
df.loc[(df['salario'] >= 6000), 'faixa_salarial'] = 'Alto'

df_final = df[['nome', 'cargo', 'salario', 'cidade', 'faixa_salarial']]

df_final.to_csv('resultado_ex05.csv', index=False)
