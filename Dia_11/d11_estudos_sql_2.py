import sqlite3

conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

# cursor.execute('SELECT * FROM funcionarios;')
# func = cursor.fetchall()

# for f in func:
#     print(f)

# # 1️⃣ COUNT — contar registros
# # Pergunta real: quantos funcionários existem?

# cursor.execute('SELECT COUNT(*) FROM funcionarios;')
# total_func = cursor.fetchone()[0]
# print(total_func)

# # Quantos moram em São Paulo?

# cursor.execute('SELECT COUNT(*) FROM funcionarios WHERE cidade = "São Paulo";')
# sp_total = cursor.fetchone()[0]
# print(sp_total)

# # 2️⃣ AVG — média salarial
# cursor.execute('SELECT AVG(salario) FROM funcionarios;')
# media_salarial = cursor.fetchone()[0]
# print(f'{media_salarial:.2f}')

# # Média salarial só de quem trabalha com Dados:
# cursor.execute('SELECT AVG(salario) FROM funcionarios WHERE cargo LIKE "%Dados%";')
# media_salarial_dados = cursor.fetchone()[0]
# print(f'{media_salarial_dados:.2f}')

# # 3️⃣ SUM — soma
# # Folha salarial total:

# cursor.execute('SELECT SUM(salario) FROM funcionarios;')
# total_salarios = cursor.fetchone()[0]
# print(f'{total_salarios:.2f}')

# # 4️⃣ GROUP BY — aqui o jogo muda
# # Salário médio por cargo:

# cursor.execute('''
# SELECT cargo, AVG(salario)
# FROM funcionarios
# GROUP BY cargo;
# ''')
               
# salario_medio_cargo = cursor.fetchall()
# for smc in salario_medio_cargo:
#     print(smc)

# # Quantidade de funcionários por cidade:

# cursor.execute('SELECT cidade, COUNT(*) FROM funcionarios GROUP BY cidade;')
# func_cidade = cursor.fetchall()
# for fc in func_cidade:
#     print(fc)

# # 5️⃣ GROUP BY + ORDER BY (bem comum)
# # Cidades com mais funcionários:

# cursor.execute('SELECT cidade, COUNT(*) AS total FROM funcionarios GROUP BY cidade ORDER BY total DESC;')
# cidades_mais_func = cursor.fetchall()
# for cmf in cidades_mais_func:
#     print(cmf)

# Extras:

# # ✍️ Exercícios (4 rápidos, dá tempo)
# # 🔹 Ex 1
# # Quantos funcionários existem por cargo?

# cursor.execute('SELECT cargo, COUNT(*) FROM funcionarios GROUP BY cargo;')
# func_por_cargo = cursor.fetchall()
# for fpc in func_por_cargo:
#     print(fpc)

# # 🔹 Ex 2
# # Qual é o salário médio por cidade?
# cursor.execute('SELECT cidade, AVG(salario) FROM funcionarios GROUP BY cidade;')
# salario_medio_cidade = cursor.fetchall()
# for smc in salario_medio_cidade:
#     print(smc)

# # 🔹 Ex 3
# # Qual cidade tem a maior folha salarial (SUM)?
# cursor.execute('SELECT cidade, SUM(salario) FROM funcionarios GROUP BY cidade ORDER BY SUM(salario) DESC;')
# cidade, total = cursor.fetchone()
# print(cidade, total)

# 🔹 Ex 4
# Quantos funcionários trabalham com Dados, por cidade?
# (dica: WHERE + GROUP BY)
cursor.execute('SELECT cidade, COUNT(*) FROM funcionarios WHERE cargo LIKE "%Dados%" GROUP BY cidade;')
func_dados_cidade = cursor.fetchall()
for fdc in func_dados_cidade:
    print(fdc)
