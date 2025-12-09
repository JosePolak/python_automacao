# TEORIA

import pandas as pd

df = pd.read_csv('dados.csv') # --> para fazer a leitura do arquivo

print(df.head()) # --> mostra as primeiras linhas para conferência de nomes de colunas, para checar se não houve alguma confusão

print(df.info()) # --> checar número de linhas e colunas e seus tipos; checar se há valores nulos

print(df.describe()) # --> estatísticas rápidas

print(df['idade']) # --> mostra toda a coluna idade

print(df[df['idade'] > 30]) # --> é possível filtrar
print(df[df['sexo'] == 'f'])
print(df[df['cidade'] == 'São Paulo'])

df['categoria'] = df['idade'] > 30 # --> criar novas colunas
print(df)

print(df['idade'].sum()) # --> somar
print(df['idade'].mean()) # --> média
