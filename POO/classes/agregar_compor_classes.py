class Contato:
    #Criando construtor
    def __init__(self, residencial, celular):
        self.residencial = residencial
        self.celular = celular
#classe cliente recebendo nome , idade e telefone(opicional)
class Cliente:
    def __init__(self, nome , idade, fone= False):
        self.nome = nome
        self.idade = idade
        self.fone =[]
        #metodo utilizado para atribuir telefones, tanto residencial como celular
    def addFone(self, residencial, celular):
        #adicionando os telefones a uma lista da classe cliente
        self.fone.append(Contato( residencial, celular))
    def listaFone(self):
        #metodo para listar os telefones por meio de um for
        for fone in self.fone:
            print(fone.residencial, fone.celular)

cliente1 = Cliente('Fernando', 32)
cliente1.addFone('129803712098', '31233123')
print(cliente1.nome)
print(cliente1.listaFone())
