# Exercício 4 — Limpeza de nomes
# 1. Padronizar a coluna nome:
# - remover espaços duplos
# - corrigir capitalização (primeira letra maiúscula)
# - eliminar números perdidos (“marcos1”, “ana3”)
# - remover sufixos estranhos (“-test”, “_temp”)
# 2. Criar df_nome_ok.

import pandas as pd
import re

df = pd.read_csv('dados_ex08.csv')

def limpar_nome(nome):
    nome = str(nome).strip().lower()
    # remover sufixos indesejados no final do nome (ex: -temp, -test, _temp, _test)
    nome = re.sub(r'[\s\-_]+(?:temp|test)$', '', nome, flags=re.IGNORECASE)
    # remover aspas, tipos diferentes de travessão, caracteres estranhos
    nome = re.sub(r"[“”\"'´`]", '', nome)
    # trocar qualquer coisa que não seja letra ou espaço por espaço
    nome = re.sub(r'[^a-zà-ú\s]', ' ', nome)
    # trocar múltiplos espaços por um só
    nome = re.sub(r'\s+', ' ', nome).strip()
    # capitalizar cada palavra
    nome = nome.title()
    return nome
# Aplicar a função de limpeza ao DataFrame
df['df_nome_ok'] = df['nome'].apply(limpar_nome)

print(df)
