# Exercício 1 — Filtrar combinações de condições
# Com o arquivo dados_ex08.csv (mesma estrutura do ex05, só que maior e mais sujo):
# 1. Filtrar somente funcionários:
# - da cidade de São Paulo
# - com salário acima de 5000
# - e cargo Analista de Dados ou Cientista de Dados
# 2. Crie df_filtro1.

import pandas as pd

df = pd.read_csv('dados_ex08.csv')

df_filtro1 = df[
    (df['cidade'].str.contains(r'sao|sp\b|sampa', case=False, regex=True)) &
    (df['salario'] > 5000) &
    (df['cargo'].str.contains(r'\b(ad)\b|\b(cd)\b|analista.*dados|analis.*dados|cientista.*dados', case=False, regex=True))
]

print(df_filtro1)
