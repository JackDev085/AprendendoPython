class Base:
    def __init__(self):
        self.dados= {}#atributo de acesso público

    def protegido(self):
        self._dados ={}#atributo que pode ser acessado pela própria classe ou subclasses e não é liberado para todos

    def protegido(self):
        self.__dados ={}#atributo que só pode ser acessado por dentro da classe

base = Base()
print(base.dados) #Mostrará o resultado
print(base._dados) #Erro
print(base.__dados) #Erro


