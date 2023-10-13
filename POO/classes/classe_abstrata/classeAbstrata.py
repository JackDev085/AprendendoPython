#Classe abstrata é uma classe que serve de "molde"
#para outras classes

#ara criar uma classe abstrata precisaremos importar
#os módulos de uma biblioteca

from abc import ABC,abstractmethod
class Pessoa(ABC): #Criação da classe abstrata pasando como parametro
    #o módulo do imporrt
    @abstractmethod #Anotation para reforçar ao interpretador todos os
    #blocos de código que vinherem em sequência nessa classe devem ser sobescritas
    #em suas respectivas classes filhas dessa hierarquia
    def logar(self):
        pass
class Usuario(Pessoa): #Aqui temos uma referência a classe abstrata como parâmetro
    def logar(self):
        print(("Usuário logado no sistema"))

pessoa2 = Usuario() #Instância de usuário que é herdado da classe pessoa
pessoa2.logar()

pessoa1 = Pessoa()
pessoa1.logar()#Aqui terá um erro pois uma classe abstrata não pode ser inicializada
#com o método "logar()"
