#para usarmos a funcao reduce precisaremos importar a biblioteca reduce de functools
from functools import reduce

#A funcao reduce () é normalmente utilizada para realizar o agrupamento dos dados de uma lista

def soma(num1, num2):
    return num1+num2

lista = [1,2,3,4,5,6,7,8,9,10] #55
#A funcao reduce() por sua vez recebe sempre dois parãmetros, que função
#será utilizada e sobre quais dados será aplicada a função, respectivamente

#Nesse caso, a ídeia é que seja realizada a soma do primeiro elemento de nossa lista com o segundo elemento, e
#este resultado será somado com o seguinte elemento, este resultado será somado com o quarto elemento
#repetindo esse processo até o último elemento da lista
resultado = reduce(soma, lista)
print(resultado)