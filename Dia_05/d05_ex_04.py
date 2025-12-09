# 4) Filtros + cálculos simples
# Filtrar apenas quem ganha acima de 3000.
# Criar coluna salario_corrigido = salário * 1.05 (reajuste de 5%).
# Mostrar apenas as pessoas com salário corrigido > 4000 usando .loc.

import pandas as pd

df = pd.read_csv('dados_sujos.csv')

df['idade'] = pd.to_numeric(df['idade'], errors='coerce')
df.loc[(df['idade'] < 0) | (df['idade'] > 120), 'idade'] = None
df['idade'] = df['idade'].astype('Int64')

# A partir daqui, exercício 02
def converte_salario(valor):
    valor = str(valor).strip().replace('R$', '').replace(' ', '')

    # --- Formato EUA: 1,234.56 ---
    if re.match(r'^\d{1,3}(,\d{3})*\.\d{2}$', valor):
        return float(valor.replace(',', ''))

    # --- Formato BR: 1.234,56 ---
    if re.match(r'^\d{1,3}(\.\d{3})*,\d{2}$', valor):
        return float(valor.replace('.', '').replace(',', '.'))

    # --- Caso tenha ponto mas NÃO tenha vírgula ---
    # Decide: é separador de milhar ou decimal?
    if '.' in valor and ',' not in valor:
        partes = valor.split('.')

        # Se a parte final tiver 2 dígitos → decimal
        if len(partes[-1]) == 2:
            return float(valor.replace(',', ''))
        else:
            # Ex.: 2.800 → 2800
            return float(valor.replace('.', ''))

    # --- Caso tenha só vírgula (BR decimal) ---
    if ',' in valor and '.' not in valor:
        return float(valor.replace('.', '').replace(',', '.'))

    # --- Caso número puro ---
    return pd.to_numeric(valor, errors='coerce')

import re
df['salario'] = df['salario'].apply(converte_salario)
df['salario_anual'] = df['salario'] * 12

# A partir daqui, exercício 03
df['nome'] = (
    df['nome']
    .astype(str)
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)
    .str.replace(r'(?<=[A-Za-z])\s+(?=[A-Za-z])', '', regex=True)
)

df.loc[df['nome'].str.contains('joao', case=False, na=False), 'nome'] = 'João'
df.loc[df['nome'].str.contains('Carolos', case=False, na=False), 'nome'] = 'Carlos'
df.loc[df['nome'].str.contains('Brunno', case=False, na=False), 'nome'] = 'Bruno'

df.loc[df['cidade'].str.contains(r'sao paulo|sao|sp', case=False, regex=True), 'cidade'] = 'São Paulo'
df.loc[df['cidade'].str.contains(r'rio de janero|janero|rj', case=False, regex=True), 'cidade'] = 'Rio de Janeiro'
df.loc[df['cidade'].str.contains(r'curitba', case=False, regex=True), 'cidade'] = 'Curitiba'

df['cidade'] = (
    df['cidade']
    .astype(str)
    .str.strip()
    .str.title()
    .str.replace(r'\s+', ' ', regex=True)
)

df['departamento'] = (
    df['departamento']
    .astype(str)
    .str.lower()
    .str.strip()
    .str.replace(r'\s+', ' ', regex=True)        # normaliza espaços
    .str.replace(r'(?<=\w)\s+(?=\w)', '', regex=True)  # remove espaço indevido dentro da palavra
    .str.title()
)

df.loc[df['departamento'].str.contains(r'\btecnologia\b|\bti\b', case=False, regex=True), 'departamento'] = 'TI'
df.loc[df['departamento'].str.contains(r'\brh\b', case=False, regex=True), 'departamento'] = 'RH'

# A partir daqui, exercício 04
salario_acima_3000 = df.loc[df['salario'] > 3000, ['nome', 'salario']]
print(salario_acima_3000)

df['salario_corrigido'] = df['salario'] * 1.05

sal_corrig_acima_4000 = df.loc[df['salario_corrigido'] > 4000, ['nome', 'salario', 'salario_corrigido']]
print(sal_corrig_acima_4000)

print(df)
