#Quando se utiliza incrementos ou contadores em python
#tem uma funcionalidade que pode ajudar muito no desempenho.

#Ele se chama count()

#primeiro vamos importar ele da biblioteca itertools
from itertools import count
contador = count()

#Aqui temos um for que percorre uma sequencia de números
#na variável count e por sua vez imprime valores até que o número impresso
#seja maior ou igual a 10
for numero in contador:
    print(numero)
    if numero >= 10:
        break
        """
        
0
1
2
3
4
5
6
7
8
9
10"""

#Aqui temos outro exemplo de seu uso, adicionando um início ao seu começo
count1 = count(start = 40)
for numero1 in count1:
    print(numero1)
    if numero1 >= 50:
        break
"""
40
41
42
43
44
45
46
47
48
49
50"""

#Aqui temos outro uso da funcao count, tendo um ponto de partida e
#um intervalo na seleção dos números

contador1 = count(start = 0, step= 2)

for numero in contador1:
    print(numero)
    if numero >= 10:
        break
#0
#1
#2
#4
#6
#8
#10