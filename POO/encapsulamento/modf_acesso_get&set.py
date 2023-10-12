class Social:
    #construtor
    def __init__(self, nome):
    #atributos de classe definidos como privados
        self.__nome = nome
        self.__logar = None
    @property
    #precisamos de um metodo público para retornar esses
    #valores privados
    def nome(self):
        return self.__nome

    # precisamos de um metodo público para retornar esses
    # valores privados
    @property
    def logar (self):
        return self.__logar

    @logar.setter
    def logar(self, logar):
        self.logar = logar