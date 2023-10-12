class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    #No caso desse método ele utiliza o atributo de um onjeto criado
    #e utiliza no corpo do seu método
    def logar(self):
        print(f'Você está logado {self.nome}')
        self.loguin = True

pessoa1 = Pessoa('jack' , 22 )
pessoa1.logar()
print(pessoa1.nome, pessoa1.idade)

if(pessoa1.loguin == True):
    print("Tudo certo")