class Usuario:
    #Método init geralmente usado para iniciar o valor de uma variável
    #geralmente tem ligação com construturo
    #Self é usado para dar referência a instancia da classe
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def boas_vindas(self):
        print(f'Usuário: {self.nome}, idade: {self.idade}')

usuario1 = Usuario(nome ='fernando' , idade = '31')
setattr(usuario1 ,'nome', 'junior')
delattr(usuario1,'idade',)
setattr(usuario1, 'idade', '22')
usuario1.boas_vindas()
