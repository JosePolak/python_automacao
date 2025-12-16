import sqlite3

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE funcionarios (
#     id INTEGER PRIMARY KEY,
#     nome TEXT,
#     cargo TEXT,
#     salario REAL,
#     cidade TEXT
# );
# ''')
# conn.commit()

# cursor.execute('''
# INSERT INTO funcionarios (nome, cargo, salario, cidade)
# VALUES
# ('Ana Silva', 'Analista de Dados', 5200, 'São Paulo'),
# ('Bruno Costa', 'Desenvolvedor Python', 6500, 'Rio de Janeiro'),
# ('Carla Souza', 'Cientista de Dados', 8200, 'São Paulo'),
# ('Daniel Lima', 'Analista de Sistemas', 4800, 'Belo Horizonte'),
# ('Eduardo Rocha', 'Engenheiro de Dados', 9000, 'São Paulo'),
# ('Fernanda Alves', 'Analista de Dados Júnior', 3500, 'Curitiba'),
# ('Gabriel Mendes', 'Desenvolvedor Web', 4200, 'Porto Alegre'),
# ('Helena Pires', 'Analista de BI', 5800, 'São Paulo'),
# ('Igor Nogueira', 'Cientista de Dados', 7800, 'Rio de Janeiro'),
# ('Juliana Freitas', 'Analista de Dados Pleno', 6100, 'Campinas'),
# ('Kleber Santos', 'DBA', 7000, 'São Paulo'),
# ('Larissa Teixeira', 'Analista Financeiro', 4600, 'São Paulo'),
# ('Marcos Vinícius', 'Engenheiro de Software', 8300, 'Recife'),
# ('Natália Azevedo', 'Analista de Dados', 5400, 'Florianópolis'),
# ('Otávio Ribeiro', 'Estagiário de Dados', 2200, 'São Paulo');
# ''')
# conn.commit()

# # 🔹 Exercício 1
# # Liste nome e salário dos funcionários com salário maior que 5000.

# cursor.execute('SELECT nome, salario FROM funcionarios WHERE salario > 5000;')
# salario_maior_5000 = cursor.fetchall()

# for f in salario_maior_5000:
#     print(f)

# # 🔹 Exercício 2
# # Liste todos os funcionários de São Paulo, ordenados pelo salário decrescente.

# cursor.execute('SELECT * FROM funcionarios WHERE cidade = "São Paulo" ORDER BY salario DESC;')
# sp_salario_desc = cursor.fetchall()

# for f in sp_salario_desc:
#     print(f)

# # 🔹 Exercício 3
# # Mostre os 3 maiores salários da empresa (nome e salário).

# cursor.execute('SELECT nome, salario FROM funcionarios ORDER BY salario DESC LIMIT 3')
# maiores_salarios = cursor.fetchall()

# for f in maiores_salarios:
#     print(f)

# # 🔹 Exercício 4
# # Liste funcionários com salário entre 3000 e 6000.

# cursor.execute('SELECT * FROM funcionarios WHERE salario BETWEEN 3000 AND 6000;')
# salario_entre_3000_6000 = cursor.fetchall()

# for f in salario_entre_3000_6000:
#     print(f)

# 🔹 Exercício 5
# Liste funcionários cujo cargo contém a palavra "Dados".

cursor.execute('SELECT * FROM funcionarios WHERE cargo LIKE "%Dados%";')
cargo_dados = cursor.fetchall()

for f in cargo_dados:
    print(f)
