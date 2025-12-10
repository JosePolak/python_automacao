# Exercício 03 — Criar coluna de nível de cargo
# Com base na coluna “cargo”:
# Estagiário
# Júnior
# Pleno
# Sênior
# Especialista
# Diretor

# Tarefas:
# 1. Criar a coluna nivel com:
#   estagiário → 0
#   júnior → 1
#   pleno → 2
#   sênior → 3
#   especialista → 4
#   diretor → 5
# 2. Usando apenas .loc.

import pandas as pd

df = pd.read_csv('dados.csv')
import re

# Exercício 01 — Ajuste de nomes com inconsistências
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

# Exercício 02
df['empresa'] = (
    df['empresa']
    .astype(str)
    .str.strip()
    .str.lower()
)

df.loc[df['empresa'].str.contains(r'g.*gle|g.*ou', case=False, regex=True), 'empresa'] = 'Google'
df.loc[df['empresa'].str.contains(r'a.*ev|a.*ve', case=False, regex=True), 'empresa'] = 'Ambev'
df.loc[df['empresa'].str.contains(r't.*la', case=False, regex=True), 'empresa'] = 'Tesla'

df['empresa_valida'] = df['empresa'].isin(['Google', 'Ambev', 'Tesla'])

# Exercício 03
df['cargo'] = (
    df['cargo']
    .astype(str)
    .str.strip()
    .str.lower()
    .str.title()
)

df.loc[df['cargo'].str.contains('junior', case=False), 'cargo'] = 'Júnior'
df.loc[df['cargo'].str.contains('senior', case=False), 'cargo'] = 'Sênior'
df.loc[df['cargo'].str.contains('estagiario', case=False), 'cargo'] = 'Estagiário'

df.loc[df['cargo'] == 'Estagiário', 'nivel'] = 0
df.loc[df['cargo'] == 'Júnior', 'nivel'] = 1
df.loc[df['cargo'] == 'Pleno', 'nivel'] = 2
df.loc[df['cargo'] == 'Sênior', 'nivel'] = 3
df.loc[df['cargo'] == 'Especialista', 'nivel'] = 4
df.loc[df['cargo'] == 'Diretor', 'nivel'] = 5

df['nivel'] = df['nivel'].astype('Int64')

print(df)
