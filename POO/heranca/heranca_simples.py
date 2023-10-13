#Herança é um recurso muito interessante para a reutilização
#de linhas código.
#
# Abaixo temos uma exemplo onde a herança pode ser usado


class Corsa:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

class Gol:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

#Exemplo com herança aplicada

class Carros:
    def __init__(self , nome , ano):
        self.nome = nome
        self.ano = ano

class Corsa(Carros):
    pass
class Corsa(Carros):
    pass