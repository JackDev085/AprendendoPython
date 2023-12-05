import json

from classe_json import caminho_arquivo, Pessoa

with open(caminho_arquivo, 'r') as arquivo:
    pessoas = json.load(arquivo)
    

