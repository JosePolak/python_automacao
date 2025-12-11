import sqlite3
import pandas as pd

# Conectar ao banco
conn = sqlite3.connect('meu_banco.db')

# Consulta
query = "SELECT * FROM funcionarios;"

# Ler para DataFrame
df = pd.read_sql_query(query, conn)

print(df)

conn.close()
