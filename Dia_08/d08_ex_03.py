# Exercício 3 — Padronizar cargos
# 1. Na coluna cargo, padronizar os valores para:
# - “Analista de Dados”
# - “Cientista de Dados”
# - “Engenheiro de Dados”
# - “Estagiário”
# - “Gerente”
# 2. Corrigir erros como:
# - “analista dados”, “analis de dados”, “AD”
# - “cientista dados”, “CD”
# - “engenh dados”, “eng. dados”
# - “estag”, “estagiario”, “stag”
# - “gerent”, “grente”, “gerente.”
# 3. Criar df_cargo_corrigido.

import pandas as pd

df = pd.read_csv('dados_ex08.csv')

df['cargo'] = (
    df['cargo']
    .astype(str)
    .str.strip()
    .str.lower()
)

df.loc[df['cargo'].str.contains(r'analista.*dados|analis.*dados|ad', case=False, regex=True), 'df_cargo_corrigido'] = 'Analista de Dados'
df.loc[df['cargo'].str.contains(r'cientista.*dados|cd', case=False, regex=True), 'df_cargo_corrigido'] = 'Cientista de Dados'
df.loc[df['cargo'].str.contains(r'engenh.*dados|eng.*dados', case=False, regex=True), 'df_cargo_corrigido'] = 'Engenheiro de Dados'
df.loc[df['cargo'].str.contains(r'estag|estagiario|stag', case=False, regex=True), 'df_cargo_corrigido'] = 'Estagiário'
df.loc[df['cargo'].str.contains(r'gerent|grente|gerente', case=False, regex=True), 'df_cargo_corrigido'] = 'Gerente'

print(df)
