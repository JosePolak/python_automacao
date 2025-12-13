import sqlite3
import pandas as pd

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('empresa.db')

# Cria o df baseado no db
df_bd = pd.read_sql_query(
    'SELECT * FROM funcionarios',
    conn
)

print(df_bd)

query_01 = '''
SELECT nome, cargo, salario
FROM funcionarios
WHERE salario > 7000
'''

df_salario_maior_7000 = pd.read_sql_query(query_01, conn)
print('\n--->  Salário > 7000 <---\n')
print(df_salario_maior_7000)

query_02 = '''
SELECT cargo, AVG(salario) AS media_salarial
FROM funcionarios
GROUP BY cargo
'''
df_media_salarial_cargo = pd.read_sql_query(query_02, conn)
print('\n--->  Média Salarial por Cargo <---\n')
print(df_media_salarial_cargo)

query_03 = '''
SELECT cidade, COUNT(*) AS total_funcionarios
FROM funcionarios
GROUP BY cidade
'''
df_cidade = pd.read_sql_query(query_03, conn)
print('\n--->  Total de Funcionários por Cidade <---\n')
print(df_cidade)
