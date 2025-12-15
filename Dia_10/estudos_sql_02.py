import sqlite3

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

# APAGA A TABELA, CASO EXISTA
cursor.execute('DROP TABLE IF EXISTS produtos')
conn.commit()

# CRIA A TABELA
cursor.execute('''
CREATE TABLE produtos(
    id INTEGER,
    nome TEXT,
    preco REAL,
    estoque INTEGER
);
''')
conn.commit() # ESCREVE OS DADOS NA TABELA (SEM ISSO, NADA FEITO)

# INSERE DADOS NA TABELA
cursor.execute('''
INSERT INTO produtos (id, nome, preco, estoque)
VALUES (1, 'Teclado', 150.00, 10);
''')

# INSERINDO VÁRIOS PRODUTOS
cursor.execute('''
INSERT INTO produtos (id, nome, preco, estoque)
VALUES
    (2,'Mouse', 80.00, 25),
    (3, 'Monitor', 1200.00, 5),
    (4, 'Cadeira', 900.00, 3);
''')
conn.commit()

# VISUALIZAR DADOS
cursor.execute('SELECT * FROM produtos;')

produtos = cursor.fetchall()

for p in produtos:
    print(p)

# VISUALIZA PRODUTOS COM ESTOQUE BAIXO
cursor.execute('''
SELECT nome, estoque
FROM produtos
WHERE estoque < 10;
''')

estoque_baixo = cursor.fetchall()

print(estoque_baixo)

# EXERCÍCIOS

# 1. Insira mais um produto
cursor.execute('''
INSERT INTO produtos (id, nome, preco, estoque)
VALUES (5, 'Notebook', 3599.90, 10);
''')
conn.commit()

# 2. Faça um SELECT que mostre apenas nome e preço
cursor.execute('''
SELECT nome, preco
FROM produtos;
''')

produtos = cursor.fetchall()

for p in produtos:
    print(p)

# FECHA A CONEXÃO
conn.close()
