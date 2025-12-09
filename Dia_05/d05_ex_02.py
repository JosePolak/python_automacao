# 2) Criar novas colunas com .loc (atribuindo valores)
# Criar uma coluna faixa assim:
# se idade < 18 → "menor"
# se idade >= 18 e < 60 → "adulto"
# se idade >= 60 → "idoso"
# Mas use apenas .loc, nada de np.where hoje.
# Criar uma coluna salario_anual usando .loc[:, 'salario_anual'] = ....

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

print(df)
