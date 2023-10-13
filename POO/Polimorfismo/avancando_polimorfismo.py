#Como o próprio nome já sugere, polimorfismo, significa que
#algo pode ter muitas formas em sua estrutura.

#polimorfismo tem uma grande referência entre classes abstratas

from abc import ABC, abstractmethod
class Pesosoa(ABC):
    @abstractmethod
    def logar(self, chaveDeSeguranca):#Aqui temos um método abstrato. Nas classes
        #Subsequentes que herdare esse método, terá uma obrigatorieadade de criarem seu método.
        #Em cada método terá um comportamento diferente. Isso é o POLIMORFISMO
        pass
class Usuario(Pesosoa):
    def logar(self, chaveDeSeguranca):#Aqui temos um polimorfismo.
        print('Usuário logado no sistema')

class Bot(Pesosoa):
    def logar(self, chaveDeSeguranca):#Aqui temos um polimorfismo.
        print('Sistema rodando em segundo plano')

user1= Usuario()
user1.logar('f7a7s8')

