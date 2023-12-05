class Pessoa:
    def __init__(self, nome,sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        

p1 = Pessoa('joao', 'guilherme')
print(p1.nome, p1.sobrenome)
        