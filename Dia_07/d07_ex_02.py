# Exercício 02 — Corrigir empresas
# A coluna “empresa” tem valores como:
# “Ambev”, “Anbev”, “Ambve”
# “Google”, “Gooogle”, “Gogle”
# “Tesla”, “Tessla”, “T3sla”

# Tarefas:
# 1. Padronizar para:
#   Ambev
#   Google
#   Tesla
# 2. Usar .str.contains() com regex estratégico.
# 3. Criar uma coluna empresa_valida com True para empresas conhecidas e False para outras.

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

print(df)
