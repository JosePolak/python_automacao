import sqlite3
import pandas as pd

# # Conectar ao banco de dados (ou criar, se não existir)
# con = sqlite3.connect('meu_banco.db')
# print('Banco criado/conectado com sucesso!')
# con.close()

# # Conectar ao banco de dados
# con = sqlite3.connect('meu_banco.db')
# cursor = con.cursor()

# # Criar tabela (se não existir)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS funcionarios (
#     id INTEGER PRIMARY KEY,
#     nome TEXT NOT NULL,
#     cidade TEXT NOT NULL,
#     cargo TEXT NOT NULL,
#     salario REAL NOT NULL
# )
# """)

# # Inserir dados na tabela
# dados = [
#     ("Ana Silva", "São Paulo", "Analista de Dados", 6500),
#     ("Carlos Souza", "Rio de Janeiro", "Cientista de Dados", 12000),
#     ("Maria Lima", "São Paulo", "AD", 5200),
#     ("João Pedro", "BH", "CD", 4800)
# ]

# cursor.executemany("""
# INSERT INTO funcionarios (nome, cidade, cargo, salario)
# VALUES (?, ?, ?, ?)
# """, dados)

# con.commit()

# print('Tabela criada e dados inseridos!')
# con.close()

# Conectar ao banco de dados
con = sqlite3.connect('meu_banco.db')

# Ler dados com SELECT para um DataFrame
df = pd.read_sql_query("SELECT * FROM funcionarios", con)

print(df)

con.close()
