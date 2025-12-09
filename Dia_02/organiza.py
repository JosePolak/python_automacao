import os
import shutil

pasta = 'arquivos'

# # Esse passo é para confirmar que os arquivos estão sendo vistos pelo Python
# for arquivo in os.listdir(pasta):
#     print(arquivo)

# # Esse passo constrói um caminho completo até o arquivo e impede que Python tente mexer em subpastas por engano
# for arquivo in os.listdir(pasta):
#     caminho = os.path.join(pasta, arquivo)

#     if os.path.isdir(caminho):
#         continue

#     print(f'Arquivo encontrado: {arquivo}')

# Agora, mudando o print, o Python identificará o tipo de arquivo
for arquivo in os.listdir(pasta):
    caminho = os.path.join(pasta, arquivo)

    if os.path.isdir(caminho):
        continue

    extensao = arquivo.split('.')[-1].lower()
    # print(arquivo, '-->', extensao)

# Agora, após identificar as extensões, partimos para a classificação por tipo
    if extensao in ['jpg', 'png', 'jpeg']:
        destino = 'img'
    elif extensao in ['pdf', 'docx',  'doc', 'txt', 'pptx', 'ppt']:
        destino = 'doc'
    elif extensao in ['csv', 'xlsx', 'xls']:
        destino = 'planilha'
    else:
        destino = 'outros'

# Isso cria as pastas automaticamente
    os.makedirs(destino, exist_ok=True)

# Move os arquivos
    shutil.move(caminho, os.path.join(destino, arquivo))

print('Arquivos organizados.')
