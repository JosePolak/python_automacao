# DIA 05 — Exercícios com .loc (nível leve → médio suave)
# 1) Seleções básicas com .loc
# Use um DataFrame simples (pode ser qualquer CSV seu) e faça:
# Mostrar apenas as linhas com idade > 30 usando .loc.
# Mostrar apenas as colunas nome e cidade usando .loc.
# Mostrar a linha de índice 5 e só a coluna salario.
# Mostrar as linhas de índice 2 até 8 e colunas nome, idade.

import pandas as pd

df = pd.read_csv('dados_sujos.csv')

# df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
# df.loc[(df['idade'] < 0) | (df['idade'] > 120), 'idade'] = None
# df['idade'] = df['idade'].astype('Int64')
# idade_maior30 = df.loc[df['idade'] > 30]
# print(idade_maior30)

# filtro = df.loc[:, ['nome', 'cidade']]
# print(filtro)

# filtro = df.loc[5:5, ['salario']]
# print(filtro)

df.loc[8] = ['Teste', 'Cidade', 0, 99, 'TI'] # cria o índice 8
filtro = df.loc[2:8, :]
print(filtro)
