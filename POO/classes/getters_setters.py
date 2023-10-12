
#Criando a classe produto que será utilizada
#para agilizar o processo de criação dos gets e sets
class Produto:
    #Construtor padrão
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

#Aqui temos nosso método get que irá por sua vez buscar o valor
    #do preco de produto e retorna o mesmo como valor_valido
    @property #Annotation para demonstrar que essa é uma propriedade
    #"Get da classe"

    def preco(self):
        return self.preco_valido
    #Método set. Ele irá atribuir o valor de preço passando por algumas atribuiçõe e até lógica.
    @preco.setter #Anotação da propriedade valor seguida do .setter para reafirmar que esse método
    #é uma propriedade set
    def preco(self, valor):
        if isinstance(valor, str):#A função construída isinstance recebe um valor e um
            # objeto de classe e retorna True se o valor for uma instância da classe.
            valor = float(valor.replace('R$',''))
        self.preco_valido = valor
    def desconto(self,percentual):
        self.preco = self.preco - (self.preco*(percentual/100))


produto1 = Produto('processador', 370)
produto1.desconto(19)

produto2 = Produto('placa mãe', ' R$ 280')
produto2.desconto(20)

print(produto1.preco)
print(produto2.preco)


