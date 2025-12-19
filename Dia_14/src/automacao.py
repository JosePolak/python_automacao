import pandas as pd
import sqlite3
import os
from datetime import datetime

# LER O CSV COM PANDAS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, '..', 'data', 'dados.csv')
DB_PATH = os.path.join(BASE_DIR, '..', 'automacao.db')

df = pd.read_csv(CSV_PATH)
print(df)

# LIMPEZA DE DADOS
df['salario'] = pd.to_numeric(df['salario'], errors='coerce')
df = df.dropna()

# CRIAR BANCO DE DADOS E TABELAS
with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE,
            departamento TEXT,
            salario REAL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_execucao TEXT,
            registros_processados INTEGER
        )
    ''')

    # INSERIR DADOS DO PANDAS NO SQLITE
    dados = df[['nome', 'departamento', 'salario']].values.tolist()

    cursor.executemany(
        'INSERT OR IGNORE INTO funcionarios (nome, departamento, salario) VALUES (?, ?, ?)',
        dados
    )

    # GERAR RELATÓRIO
    cursor.execute('''
        SELECT nome, departamento, salario
        FROM funcionarios
        WHERE salario > ?
        ''', (6000,))

    relatorio = cursor.fetchall()

    print('\nRelatório - Salários acima de 6000:')
    for r in relatorio:
        print(r)

    # SALVAR LOG DA EXECUÇÃO
    cursor.execute('''
        INSERT INTO logs (data_execucao, registros_processados)
        VALUES (?, ?)
        ''', (datetime.now().isoformat(), len(df)))
