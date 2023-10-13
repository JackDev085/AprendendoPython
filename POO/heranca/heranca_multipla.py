#Assim como podemos herdar uma classe, em python temos
#como herdar duas classes ao mesmo tempo com herança múltipla


class Mercadoria:
    def __init__(self, nome , preco):
        self.nome = nome
        self.preco = preco


class Carnes(Mercadoria):
    def __init__(self, tipo , peso):
        self.tipo = tipo
        self.peso =peso

class Utensilios:
    def __init__(self, espetos, carvao):
        self.espetos = espetos
        self.carvao = carvao
    #Aqui temos um exemplo de herança múltipla
class KitChurrasco(Carnes, Utensilios):
    pass

pacote1 = KitChurrasco('carne',14.90)
pacote1.tipo = ('costela')
pacote1.peso = 1
pacote1.espetos =1
pacote1.carvao = 1
