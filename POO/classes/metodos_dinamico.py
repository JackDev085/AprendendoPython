#Métodos dinâmic são métodos que a própria classe tem que "chamar
class Pessoa:
    #Iniciando um atributo de classe e dando um valor
    ano_atual = 2023
#Contrutor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #Anotation para demonstrar que esse é um método dinâmic de classe
    @classmethod
    #Aqui temo sum método que recebe por parãmetro uma classe, seu respectivo nome de objeto e data de nasc
    def ano_nascimento(cls, nome, ano_nascimetento):
        idade = cls.ano_atual - ano_nascimetento
        return  cls(nome, idade)


pessoa2 = Pessoa.ano_nascimento('Jack', 2001)

print(pessoa2.idade)




