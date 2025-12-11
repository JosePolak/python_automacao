# Exercício 6 — Gerar o df_final
# 1. Montar o dataframe final com as seguintes colunas limpas:
# - nome
# - cargo
# - cidade
# - salario
# - faixa_salarial
# 2. E salvar como df_final.

import pandas as pd
import re

df = pd.read_csv('dados_ex08.csv')

# Exercício 2 — Corrigir erros de cidade
df['cidade'] = (
    df['cidade']
    .astype(str)
    .str.strip()
    .str.lower()
)

df.loc[df['cidade'].str.contains(r'sao.*|sp|sampa', case=False, regex=True), 'df_cidade_corrigida'] = 'São Paulo'
df.loc[df['cidade'].str.contains(r'rio.*ro|rj|rio', case=False, regex=True), 'df_cidade_corrigida'] = 'Rio de Janeiro'
df.loc[df['cidade'].str.contains(r'bel.*|bh', case=False, regex=True), 'df_cidade_corrigida'] = 'Belo Horizonte'

# Exercício 3 — Padronizar cargos
df['cargo'] = (
    df['cargo']
    .astype(str)
    .str.strip()
    .str.lower()
)

df.loc[df['cargo'].str.contains(r'analista.*dados|analis.*dados|\b(ad)\b', case=False, regex=True), 'df_cargo_corrigido'] = 'Analista de Dados'
df.loc[df['cargo'].str.contains(r'cientista.*dados|cd', case=False, regex=True), 'df_cargo_corrigido'] = 'Cientista de Dados'
df.loc[df['cargo'].str.contains(r'engenh.*dados|eng.*dados', case=False, regex=True), 'df_cargo_corrigido'] = 'Engenheiro de Dados'
df.loc[df['cargo'].str.contains(r'estag|estagiario|stag', case=False, regex=True), 'df_cargo_corrigido'] = 'Estagiário'
df.loc[df['cargo'].str.contains(r'gerent|grente|gerente', case=False, regex=True), 'df_cargo_corrigido'] = 'Gerente'

# Exercícios 4
def limpar_nome(nome):
    nome = str(nome).strip().lower()
    # remover sufixos indesejados no final do nome (ex: -temp, -test, _temp, _test)
    nome = re.sub(r'[\s\-_]+(?:temp|test)$', '', nome, flags=re.IGNORECASE)
    # remover aspas, tipos diferentes de travessão, caracteres estranhos
    nome = re.sub(r"[“”\"'´`]", '', nome)
    # trocar qualquer coisa que não seja letra ou espaço por espaço
    nome = re.sub(r'[^a-zà-úç\s]', ' ', nome)
    # trocar múltiplos espaços por um só
    nome = re.sub(r'\s+', ' ', nome).strip()
    # capitalizar cada palavra
    nome = nome.title()
    return nome
# Aplicar a função de limpeza ao DataFrame
df['df_nome_ok'] = df['nome'].apply(limpar_nome)

# Exercício 5 — Criar faixa salarial
def categoria_faixa_salarial(s):
    return (
        'Baixa' if s < 3000 else
        'Média' if s <= 7000 else
        'Alta'
    )

df['df_faixa_ok'] = df['salario'].apply(categoria_faixa_salarial)

# Exercício 6 — Gerar o df_final
df_final = df[['df_nome_ok', 'df_cargo_corrigido', 'df_cidade_corrigida', 'salario', 'df_faixa_ok']].copy()
df_final.columns = ['nome', 'cargo', 'cidade', 'salario', 'faixa_salarial']

df_final.to_csv('df_final.csv', index=False)


