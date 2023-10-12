'''Heranca tem um papek importante no mundo da orientação a objeto. Seu uso pode facilitar
tanto o aproveitamento de código como diminuir possiveis redundâncias'''

#aqui temos uma classe pai chamada carros com o atributo nom e cor
class Carros():
    #Construtor que recebe um objeto do tipo carro
    def __init__(self, nome, cor ):
        #Atribuiçoes das variaveis de instancas, aos atributos de classe.
        self.nome = nome
        self.cor = cor
    #Metodo para descrever as informações do carro
    def descricao(self):
        print(f'O carro {self.nome} tem a cor {self.cor} ')
#Aqui temos uma classe "filha" que recebe o pai em parenteses
class Gol(Carros):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
#Aqui temos outra classe "filha" que recebe o pai em parenteses
class Corsa(Carros):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

#Instanciando um carro do tipo corsa
corsa =Corsa('Baby', 'Verde')
corsa.descricao()

