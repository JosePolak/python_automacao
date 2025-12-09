import pandas as pd
import numpy as np

df = pd.read_csv('dados.csv')

# df['salario_anual'] = df['salario'] * 12
# print(df)
df.loc[:, 'salario_anual'] = df['salario'] * 12
print(df)
print('\n')

# df['categoria'] = np.where(df['salario'] > 8000, 'Senior', np.where(df['salario'] > 5000, 'Pleno', 'Junior'))
# print(df)
df.loc[df['salario'] > 8000, 'categoria'] = 'Senior'
df.loc[(df['salario'] <= 8000) & (df['salario'] > 5000), 'categoria'] = 'Pleno'
df.loc[df['salario'] <= 5000, 'categoria'] = 'Junior'
print(df)
print('\n')

df_sem_sexo = df.drop(columns=['sexo'])
print(df_sem_sexo)

df_sem_sexo.to_csv('resultado.csv', index=False)
