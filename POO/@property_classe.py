class Carro:
    def __init__(self, nome):
        self._nomeCarro = nome
        
    @property
    def getName(self):
        return self._nomeCarro

    @getName.setter
    def setName(self, valor):
        self._nomeCarro = valor
    
carro = Carro('Fiesta')
carro.setName = 'Uno'
print(carro.getName)
