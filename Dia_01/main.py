import pandas as pd

df = pd.read_csv('dados.csv')
print(df)

print('\nPessoas com idade acima de 25:')
filtro = df[df['idade'] > 25]
print(filtro)

df['maior_idade'] = df['idade'] >= 18
print('\n--- DataFrame com nova coluna ---')
print(df)

df.to_csv('resultado.csv', index=False)
print('\nArquivo "resultado.csv" salvo com sucesso!')
