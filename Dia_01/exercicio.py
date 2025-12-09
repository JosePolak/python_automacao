import pandas as pd
import numpy as np

df = pd.read_csv('dados.csv')
print(df)

print('\nPessoas com idade acima de 30 anos:')
filtro = df[df['idade'] > 30]
print(filtro)

df['categoria'] = np.where(df['idade'] >= 18, 'Adulto', 'Jovem')
print('\n--- DataFrame com nova coluna ---')
print(df)

df.to_csv('filtrado.csv', index=False)
print('\nArquivo "filtrado.csv" salvo com sucesso!')
