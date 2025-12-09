# EXERCÍCIO 2 — Criando nova coluna com .loc
# Crie uma coluna 'categoria_idade'

import pandas as pd

df = pd.read_csv('dados.csv')

# df['categoria_idade'] = 'menor' # atribui valor inicial a todos
df.loc[df['idade'] < 18, 'categoria_idade'] = 'menor' # evita iniciar com valor padrão
df.loc[df['idade'] >= 18, 'categoria_idade'] = 'adulto'
print(df)

# OBSERVAÇÃO:
# É possível usar função para reaproveitar depois
# def classifica_idade(x):
#     return 'adulto' if x >= 18 else 'menor'

# df['categoria_idade'] = df['idade'].apply(classifica_idade)
