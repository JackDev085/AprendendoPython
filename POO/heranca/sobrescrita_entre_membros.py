#A sobrescrita é nada mais que a utilização de um método parecido
#entretanto com uma scrita diferente e um comportamento diferente

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    # Na classe pessoa temos um método (acao1) com acão de 'está dormindo'
    def acao1(self):
        print(f'{self.nome} está dormindo')

class Jogador1(Pessoa):
    # Na classe Jogador1 temos um método (acao2) com acão de 'está comendo'
    def acao2(self):
        print(f'{self.nome} está comendo')

#Já na classe SaveJogador1 temos uma sobreescrita do método Pessoa com a mesma assinatura.
#Se o objeto instanciado for do tipo SaveJogador1. O método dessa classe terá
#precedência no seu uso
class SaveJogador1(Jogador1):
    def acao1(self):
        print(f'{self.nome} está acordado')

#Entretanto podemos usar essa sobrescrita utilizando o
#método da classe mãe. Ou seja utilizando o método da classe mãe
#apenas usando a declaração super
class SaveJogador2(Jogador1):
    def acao1(self):
        #Aqui estamos utilizando o conteúdo da classe
        #mae e adicionando a essa classe apenas usando
        #essa palavra reservada seguida do método
        super().acao1()
        print(f'{self.nome} está acordado')

#Instância de SaveJogador1
p1 = SaveJogador1('Fernando')
p1.acao1()
p1.acao2()

#Instância de SaveJogador2
p2 = SaveJogador2('Fernando')
p2.acao1()
p2.acao2()


