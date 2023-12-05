import json
caminho_arquivo = 'text.json'
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
p1 =Pessoa('Roberto', 45)
p2 =Pessoa('julia', 25)
p3 =Pessoa('carlos', 15)
lista_pessoas = [p1.__dict__, p2.__dict__, p3.__dict__]

with open(caminho_arquivo, 'w') as arquivo:
    json.dump(lista_pessoas, arquivo,ensure_ascii=False, indent=2)


with open(caminho_arquivo,'r',encoding='utf8') as arquivo:
    dados = json.load(arquivo)
    print(dados)
