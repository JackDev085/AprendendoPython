class Carro:
    def __init__(self, nome):
        self._nome = nome
        self._motor = None
        self._fabricante = None
    @property
    
    def carro(self):
        return self._nome
    @property
    def motor(self):
        return self._motor
        
    @motor.setter
    def motor(self, nome_motor):
        self._motor = nome_motor
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome_fabricante):
        self._fabricante = nome_fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome
        
class Fabricante:
    def __init__(self, nome_fabricante):
        self.nome = nome_fabricante

car = Carro('Fiesta')
mot = Motor('100 cavalos')
fab = Fabricante('Toyota')

car.fabricante = fab
car.motor = mot

print(car.carro)
print(car.motor.nome)
print(car.fabricante.nome)