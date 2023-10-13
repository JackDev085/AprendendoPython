#Em uma aplicação uma super classe pode ter herança
#e essas classes filhas por herdar outras clases.
#Pensando nisso tem que ter um cuidado dobrado ao fazer isso
#Pois temos que manter o código bem estruturado e coeso


##aqui temos um "mal" exemplo da herança sendo usada.
class Carros:
    def __init__(self,nome, ano):
        self.nome = nome
        self.ano = ano

class Gasolina(Carros):
    def __init__(self, tipoGasolina = True, tipoAlcool = True):
        self.tipoGasolina = tipoGasolina
        self.tipoAlcool = tipoAlcool
#Aparentemente gasolina tem a ver com um carro mas o jeep
#teria que herdar o próprio carro e não uma herança de carro
#que por sua vez se dá pela gasolina. Se tornando ineficiente
class Jeep(Gasolina):
    pass
