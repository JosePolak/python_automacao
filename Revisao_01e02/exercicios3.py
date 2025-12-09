import pandas as pd

df = pd.read_csv('dados.csv')

filtro_idade = df[df['idade'] > 30]
print(filtro_idade)

resultado = df[(df['idade'] > 25) & (df['salario'] < 5000)]
print(resultado)

df2 = df[['nome', 'idade']]
print(df2)

df_rj = df[df['cidade'] == 'Rio de Janeiro'][['nome', 'idade', 'cidade']]
print(df_rj)
