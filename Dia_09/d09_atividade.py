import pandas as pd
import sqlite3


df = pd.read_csv('funcionarios.csv')

# filtro: funcionários com salário > x
def filtrar_salario(df, salario_min):
    return df[df['salario'] > salario_min]

# filtro: funcionários com cargo 'Analista de Dados'
def filtrar_cargo(df, cargo):
    return df[df['cargo'] == cargo]

# filtro: funcionários da cidade 'São Paulo'
def filtrar_cidade(df, cidade):
    return df[df['cidade'] == cidade]

df_filtro_salario = filtrar_salario(df, 6000)
df_filtro_cargo = filtrar_cargo(df, 'Analista de Dados')
df_filtro_cidade = filtrar_cidade(df, 'São Paulo')

print('\n--->  Salário > 6000 <---\n')
print(df_filtro_salario)
print('\n--->  Cargo: Analista de Dados <---\n')
print(df_filtro_cargo)
print('\n--->  Cidade: São Paulo <---\n')
print(df_filtro_cidade)


# ----->  ATIVIDADES COM SQLITE  <-----

# Cria o db
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Cria a tabela funcionarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cargo TEXT,
    cidade TEXT,
    salario REAL
)
''')

conn.commit()

# Limpa a tabela antes de inserir novos dados
cursor.execute('DELETE FROM funcionarios')
conn.commit()

# Insere o df no banco (loop)
for _, row in df.iterrows():
    cursor.execute('''
    INSERT INTO funcionarios (nome, cargo, cidade, salario)
    VALUES (?, ?, ?, ?)
    ''', (
        row['nome'],
        row['cargo'],
        row['cidade'],
        row['salario']
    ))

conn.commit()

cursor.execute('SELECT * FROM funcionarios')
dados = cursor.fetchall()
print('\n--->  Dados da tabela funcionarios <---\n')

for linha in dados:
    print(linha)

conn.close()
