import pandas as pd

df = pd.read_csv('dados.csv')

print(df['nome'])

print(df.head())

print(df.describe())

# Filtrar quem tem idade > 30
print(df[df['idade'] > 30])

# Filtrar salário menor que 5000
print(df[df['salario'] < 5000])

# Filtros múltiplos
# & == and   e   | = or
print(df[(df['idade'] > 30) & (df['salario'] < 5000)])
print(df[(df['cargo'] == 'analista') | (df['cargo'] == 'estagiário')])

# Selecionar colunas específicas
print(df[['nome', 'idade', 'cargo']])

# A) Filtrar pessoas acima de X anos
x = int(input('Filtrar acima de qual idade? '))
df_filtrado = df[df['idade'] > x]
print(df_filtrado)

# B) Criar um novo DataFrame com nome + idade
df2 = df[['nome', 'idade']]
print(df2)

# C) Contar quantas pessoas têm salário acima de Y
y = float(input('Filtrar salários acima de: '))
resultado = df[df['salario'] > y]
print(len(resultado))
