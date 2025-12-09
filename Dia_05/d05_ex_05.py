# 5) Mini-desafio final (bem suave)
# Dado um DataFrame com colunas:
# nome
# cidade
# salario
# cargo
# Faça apenas com .loc:
# Selecionar somente os analistas de dados que ganham < 4000.
# Aumentar o salário deles em 8%, criando uma coluna novo_salario.
# Filtrar apenas os de São Paulo e mostrar nome + novo_salario.

import pandas as pd

df = pd.read_csv('dados_ex05.csv')

ad_menor4000 = df.loc[(df['cargo'] == 'Analista de Dados') & (df['salario'] < 4000)]

df.loc[
    (df['cargo'] == 'Analista de Dados') & (df['salario'] < 4000), 'novo_salario'
    ] = df['salario'] * 1.08

ad_sp = df.loc[(df['cidade'] == 'São Paulo') & df['novo_salario'].notna(), ['nome', 'novo_salario']]

print(df)
print(ad_sp)
