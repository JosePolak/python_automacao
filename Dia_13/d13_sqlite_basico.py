import sqlite3

conn = sqlite3.connect('dia13.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        idade INTEGER
    );
''')
# Obs.: IF NOT EXISTS --> evita erros se rodar o script mais de uma vez

# LIMPA A TABELA
cursor.execute("DELETE FROM pessoas")
conn.commit()

# INSERE DADOS
pessoas = [
    ('Ana', 30),
    ('Bruno', 25),
    ('Carlos', 40)
]

cursor.executemany('INSERT OR IGNORE INTO pessoas (nome, idade) VALUES (?, ?);',
    pessoas
)
conn.commit()

# CONSULTA
cursor.execute('SELECT * FROM pessoas;')
resultado = cursor.fetchall()

for p in resultado:
    print(p)
