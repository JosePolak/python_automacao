import sqlite3

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

# # Bloco 1 - Exercício 1
# cursor.execute('DROP TABLE IF EXISTS produtos')
# conn.commit()

# # Bloco 1 - Exercício 2
# cursor.execute('''
# CREATE TABLE produtos(
#     id INTEGER,
#     nome TEXT,
#     preco REAL,
#     estoque INTEGER);
# ''')
# conn.commit()

# # Bloco 2 - Exercício 3
# cursor.execute('''
# INSERT INTO produtos(id, nome, preco, estoque)
# VALUES
#     (1, 'Notebook', 3499.99, 7),
#     (2, 'Monitor 19"', 789.00, 3),
#     (3, 'Mouse pad', 35.00, 99);
# ''')
# conn.commit()

# # Bloco 2 - Exercicio 4
# cursor.execute('''
# INSERT INTO produtos(id, nome, preco, estoque)
# VALUES
#     (4, 'Mouse s/ fio', 79.90, 50),
#     (5, 'Teclado c/ fio', 99.90, 0);
# ''')
# conn.commit()

# # Bloco 3 - Exercício 5
# cursor.execute('SELECT * FROM produtos;')
# produtos = cursor.fetchall()
# for p in produtos:
#     print(p)

# # Bloco 3 - Exercício 6
# cursor.execute('SELECT nome, preco FROM produtos;')
# produtos = cursor.fetchall()
# for p in produtos:
#     print(p)

# # Bloco 4 - Exercício 7
# cursor.execute('SELECT * FROM produtos WHERE estoque < 10;')
# produtos = cursor.fetchall()
# for p in produtos:
#     print(p)

# # Bloco 4 - Exercício 8
# cursor.execute('SELECT * FROM produtos WHERE preco > 1000;')
# produtos = cursor.fetchall()
# for p in produtos:
#     print(p)

# # Bloco 5 - Exercício 9
# cursor.execute('SELECT nome, estoque FROM produtos WHERE estoque < 5 OR preco > 2000')
# produtos = cursor.fetchall()
# for p in produtos:
#     print(p)

# Bloco 6 - Exercício 10
cursor.execute('SELECT nome, estoque FROM produtos WHERE estoque < 5 OR preco > 2000')
produtos = cursor.fetchall()

for p in produtos:
    print(p)
