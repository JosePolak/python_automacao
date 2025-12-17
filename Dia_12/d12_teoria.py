# -------------------------------------------------------

# ⚠️ Regras importantes (não pule)

#  Não usar f-string em SQL

#  Sempre usar placeholders ?

#  Nunca fazer UPDATE ou DELETE ---> sem <--- WHERE

#  Commit após qualquer alteração

# -------------------------------------------------------


# 1️⃣ INSERT — Inserindo dados do jeito certo
# Exemplo base

# Suponha esta tabela:

# CREATE TABLE produtos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT,
#     preco REAL,
#     categoria TEXT
# );

# Inserção correta (com placeholder)

# cursor.execute("""
#     INSERT INTO produtos (nome, preco, categoria)
#     VALUES (?, ?, ?)
# """, ("Mouse", 79.90, "Periféricos"))

# conn.commit()

# 📌 Por que assim?

# - evita SQL Injection

# - evita erro de aspas

# - permite reutilizar código

# ❌ Nunca faça:

# cursor.execute(f"INSERT INTO produtos VALUES ('{nome}', {preco})")

# 2️⃣ INSERT múltiplo (muito comum em automação)

# produtos = [
#     ("Teclado", 129.90, "Periféricos"),
#     ("Monitor", 899.00, "Vídeo"),
#     ("Cabo HDMI", 29.90, "Acessórios")
# ]

# cursor.executemany("""
#     INSERT INTO produtos (nome, preco, categoria)
#     VALUES (?, ?, ?)
# """, produtos)

# conn.commit()

# ✔️ Rápido
# ✔️ Limpo
# ✔️ Profissional

# 3️⃣ UPDATE — Atualizando com segurança

# Atualizar UM registro

# cursor.execute("""
#     UPDATE produtos
#     SET preco = ?
#     WHERE nome = ?
# """, (99.90, "Mouse"))

# conn.commit()

# 🚨 Regra de ouro

# UPDATE sem WHERE = desastre

# ❌ Jamais:

# UPDATE produtos SET preco = 0;

# 4️⃣ DELETE — Excluir sem arrependimento

# Excluir registro específico

# cursor.execute("""
#     DELETE FROM produtos
#     WHERE nome = ?
# """, ("Cabo HDMI",))

# conn.commit()

# 📌 Atenção ao detalhe:

# - a tupla precisa da vírgula → ("Cabo HDMI",)

# 5️⃣ Erros comuns (importantíssimo)

# 🔴 Esquecer o commit()

# ➡️ Código “funciona”, mas nada salva.

# 🔴 Atualizar sem WHERE

# ➡️ Perda total de dados.

# 🔴 Deletar antes de testar

# ➡️ Sempre teste antes:

# SELECT * FROM produtos WHERE nome = 'Cabo HDMI';
