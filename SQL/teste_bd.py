import sqlite3

#Conectar a um banco em memória (só existe enquanto o script roda)
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Criar uma tabela de exemplo: funcionarios
cursor.execute('''
CREATE TABLE funcionarios (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    cargo TEXT,
    salario REAL
)
''')

conn.commit()
print('Tabela criada!')

# Inserir dados na tabela funcionarios
funcionarios = [
    (1, 'Ana', 'Analista', 5000),
    (2, 'Bruno', 'Desenvolvedor', 7000),
    (3, 'Carla', 'Designer', 4500),
    (4, 'Diego', 'Analista', 5200)
]
cursor.executemany('INSERT INTO funcionarios VALUES (?, ?, ?, ?)', funcionarios)
conn.commit()
print('Registros inseridos!')

# Selecionar todos os funcionários
cursor.execute('SELECT * FROM funcionarios')
print(cursor.fetchall())

# Selecionar nomes e cargos
cursor.execute('SELECT nome, cargo FROM funcionarios')
print(cursor.fetchall())

# Selecionar funcionários com salário maior que 5000
cursor.execute('SELECT nome, salario FROM funcionarios WHERE salario > 5000')
print(cursor.fetchall())

# Analistas
cursor.execute("SELECT * FROM funcionarios WHERE cargo = 'Analista'")
print(cursor.fetchall())

# Aumentar o salário de Ana
cursor.execute("UPDATE funcionarios SET salario = salario + 500 WHERE nome = 'Ana'")
conn.commit()

# Deletar Diego
cursor.execute("DELETE FROM funcionarios WHERE nome = 'Diego'")
conn.commit()

# Verificar alterações
cursor.execute('SELECT * FROM funcionarios')
print(cursor.fetchall())

# Funções agregadas: COUNT()
cursor.execute('SELECT COUNT(*) FROM funcionarios')
print('Total de funcionários:', cursor.fetchone()[0])

# Funções agregadas: AVG()
cursor.execute('SELECT AVG(salario) FROM funcionarios')
print('Salário médio:', cursor.fetchone()[0])

# Atividade 1 — Filtragem e ordenação
# Mostre todos os funcionários cujo salário seja maior que 4800.
# Ordene o resultado pelo salário em ordem decrescente.
# Dica: use WHERE + ORDER BY DESC.

cursor.execute('SELECT * FROM funcionarios WHERE salario > 4800 ORDER BY salario DESC')
print('Funcionários com salário maior que 4800, ordenados por salário descrescente:')
print(cursor.fetchall())

# Atividade 2 — Atualização e contagem
# Aumente em 10% o salário de todos os funcionários com cargo Analista.
# Conte quantos funcionários têm salário agora maior que 5000.
# Dica: use UPDATE e depois SELECT COUNT(*).

cursor.execute("UPDATE funcionarios SET salario = salario * 1.10 WHERE cargo = 'Analista'")
conn.commit()
cursor.execute('SELECT * FROM funcionarios')
print(cursor.fetchall())

cursor.execute('SELECT COUNT(*) FROM funcionarios WHERE salario > 5000')
print('Número de funcionários com salário maior que 5000 após o aumento:', cursor.fetchone()[0])
