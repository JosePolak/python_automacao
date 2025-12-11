# Exercício 5 — Criar coluna de faixa salarial
# 1. Criar faixa_salarial com base em:
# - "Baixa" → salário < 3000
# - "Média" → 3000 a 7000
# - "Alta" → > 7000
# 2. Criar df_faixa_ok.

import pandas as pd

df = pd.read_csv('dados_ex08.csv')

def categoria_faixa_salarial(salario):
    if salario < 3000:
        return 'Baixa'
    elif 3000 <= salario <= 7000:
        return 'Média'
    else:
        return 'Alta'

df['df_faixa_ok'] = df['salario'].apply(categoria_faixa_salarial)

print(df)
