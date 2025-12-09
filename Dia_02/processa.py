# 1. Leia todos os arquivos .csv que estiverem dentro da pasta exercicios.

import os
import pandas as pd

# # PASSO 01 - Lê automaticamente todos os arquivos CSV na pasta exercicios
# pasta = 'exercicio'
# # os.listdir() --> identificará os arquivos (no caso, .csv) na pasta indicada
# for arq in os.listdir(pasta):
#     if arq.endswith('.csv'):
#         print(arq)

# PASSO 02 - Lê automaticamente cada CSV e guarda em uma lista
pasta = 'exercicio'
lista_dfs = []

for arq in os.listdir(pasta):
    if arq.endswith('.csv'):
        caminho = os.path.join(pasta, arq)
        df = pd.read_csv(caminho)
        lista_dfs.append(df)

# for tabela in lista_dfs:
#     print(tabela)
#     print('-' * 30)

# PASSO 3 - Concatena todos os DFs em um só
df_final = pd.concat(lista_dfs, ignore_index=True)

# print('DATAFRAME FINAL UNIFICADO:')
# print(df_final)

# PASSO 4A - Pessoas com idade acima de 30 anos
acima30 = df_final[df_final['idade'] > 30]
print('\nPessoas acima de 30 anos:')
print(acima30)

# PASSO 4B - Pessoas menores de idade (idade < 18)
menores = df_final[df_final['idade'] < 18]
print('\nMenores de idade:')
print(menores)

# PASSO 4C - Criar uma coluna 'categoria' classificando:
df_final['categoria'] = df_final['idade'].apply(
    lambda x: 'Adulto' if x >= 18 else 'Jovem'
)

print('\nTabela com categorias:')
print(df_final)

# PASSO 5 — Exporta tudo automaticamente
# Exportações automáticas
acima30.to_csv(os.path.join(pasta, 'acima30.csv'), index=False)
menores.to_csv(os.path.join(pasta, 'menores.csv'), index=False)
df_final.to_csv(os.path.join(pasta, 'tabela_final.csv'), index=False)

print('\nArquivos exportados com sucesso!')
