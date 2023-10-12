# Um método estático é um método que não tem
#isnstâncias por parametro sendo, assim um metodo acessivel
# e instanciável por qualquer objeto

from random import randint

class Rand:
    #Aqui temos uma anotação para definir que esse método é um
    #metódo estático
    @staticmethod
    def gerador_id():
        #Esse méthodo randint(a , b) percorre um número aleatório entre 100 e 999
        gerador = randint(100, 999)
        return gerador

print(Rand.gerador_id())

