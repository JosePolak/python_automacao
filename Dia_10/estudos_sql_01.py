import sqlite3

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

# Exercício 01
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER,
    nome TEXT,
    preco REAL
);
''')
conn.commit()


# Exercício 02
cursor.execute('''
DROP TABLE produtos;
''')
conn.commit()


# Exercício 03
cursor.execute('''
CREATE TABLE produtos(
    id INTEGER,
    nome TEXT,
    preco REAL,
    estoque INTEGER
);
''')
conn.commit()

conn.close()
