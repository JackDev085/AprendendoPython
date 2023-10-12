#o mmétodo construtur é ativado ao ser instanciado um objeto de uma classe
#por padrao é criado um método construtor vazio ao criar uma classe

#Exemplo de método contrutor da classe Pessoa
class Pessoa():
    #Método de classe
    def __init__(self , nome , idade, sexo):
        #Atritubutos de classe
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


#Instância da clasee
pessoa1 = Pessoa('fernando', 22, 'M')

print(f'Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Sexo: {pessoa1.sexo}')