import sqlite3

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

# cursor.execute('''CREATE TABLE produtos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT,
#     preco REAL,
#     categoria TEXT
# );
# ''')

# 🟦 Exercício 1 — INSERT (registro único)
#  - Inserir 1 produto usando execute() e placeholders ?
#  - Usar commit() após a inserção

# cursor.execute('''
#     INSERT INTO produtos (nome, preco, categoria)
#     VALUES (?, ?, ?)
# ''', ('Mouse', 79.90, 'Periféricos'))
# conn.commit()

# 🟦 Exercício 2 — INSERT múltiplo
#  - Criar uma lista com 3 produtos
#  - Inserir todos de uma vez usando executemany()
#  - Usar placeholders corretamente
#  - Executar commit()

# produtos = [
#     ('Teclado', 129.90, 'Periféricos'),
#     ('Monitor', 899.00, 'Vídeo'),
#     ('Cabo HDMI', 29.90, 'Acessórios')
# ]

# cursor.executemany('''
#     INSERT INTO produtos (nome, preco, categoria)
#     VALUES (?, ?, ?)
# ''', produtos)
# conn.commit()

# 🟨 Exercício 3 — UPDATE
#  - Escolher 1 produto existente
#  - Atualizar apenas o preço
#  - Usar WHERE corretamente
#  - Executar commit()

# cursor.execute('''
#     UPDATE produtos
#     SET preco = ?
#     WHERE nome = ?
# ''', (99.90, 'Mouse'))
# conn.commit()

# 🟥 Exercício 4 — DELETE
#  - Excluir apenas 1 produto específico
#  - Garantir que o WHERE esteja correto
#  - Executar commit()

# cursor.execute('''
#     DELETE FROM produtos
#     WHERE nome = ?
# ''', ('Cabo HDMI',))
# conn.commit()

cursor.execute('SELECT * FROM produtos;')
produtos = cursor.fetchall()
for p in produtos:
    print(p)
