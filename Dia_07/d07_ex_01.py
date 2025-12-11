# Exercício 01 — Ajuste de nomes com inconsistências
# No arquivo dados_ex07.csv, alguns nomes estão assim:
# JOSE SILVA
# Maria_souza
# ana—beatriz
# CARLOS ALMEIDA
# “ joao pedro ”

# Tarefas:
# 1. Padronizar tudo para “Nome Sobrenome”, capitalizado.
# 2. Remover underscores, múltiplos espaços e qualquer caractere estranho.
# 3. Criar uma coluna com o primeiro nome e outra com o sobrenome.

import pandas as pd
import re

df = pd.read_csv('dados.csv')

def limpar_nome(nome):
    nome = str(nome).strip().lower()
    # remover aspas, tipos diferentes de travessão, caracteres estranhos
    nome = re.sub(r'[“”"\'´`]', '', nome)
    # trocar qualquer coisa que não seja letra ou espaço por espaço
    nome = re.sub(r'[^a-zà-ú\s]', ' ', nome)
    # trocar múltiplos espaços por um só
    nome = re.sub(r'\s+', ' ', nome).strip()
    # capitalizar
    nome = nome.title()
    return nome

# Aplicar a função de limpeza ao DataFrame
df['nome_limpo'] = df['nome'].apply(limpar_nome)

# Separar primeiro nome e sobrenome
df['primeiro_nome'] = df['nome_limpo'].str.split().str[0]
df['sobrenome'] = df['nome_limpo'].str.split().str[-1]

print(df)
