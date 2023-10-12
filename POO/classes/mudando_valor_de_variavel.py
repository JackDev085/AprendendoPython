class Usuario:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def boas_vindas(self):
        print(f'Usuário: {self.nome}, idade: {self.idade}')

usuario1 = Usuario(nome ='fernando' , idade = '31')
usuario1.nome = 'fernando gustavo' 
usuario1.boas_vindas()
print(usuario1.nome)