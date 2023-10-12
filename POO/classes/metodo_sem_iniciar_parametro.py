#Criando classe pessoa

class Pessoa():
    def __init__(self, nome,idade,sexo=False, altura =False):#atribuindo os parametros
        #como false estamos habilitando-os como opicionais
        self.nome = nome
        self.idade = idade
        self.sexo = idade #Essa variável inicirá com none
        self.altura=altura #Essa variável inicirá com none

pessoa1 = Pessoa('ricardo' ,22 , 'M', 1.68)
pessoa2 = Pessoa('joao' ,12) #O compilador não obriga que seja colocado
#todos os dados ao instanciar o objeto

print(pessoa1.idade, pessoa1.nome,pessoa1.sexo,pessoa1.altura)
print(pessoa2.idade, pessoa2.nome)