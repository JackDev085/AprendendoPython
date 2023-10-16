#Aqui atribuimos a biblioteca random que por sua vez foi
#atribuido o nome de ra

import random as ra

#Aqui podemos usar a mesma biblioteca com o nome que
#escolhemos ao importar
print(ra.randint(1,10))

#Caso quisermos usar apenas uma função de uma biblioteca
#´é interassente em termos de desempenho importar apenas
#a função requerida. Ex a baixo

from math import sqrt as raiz_quadrada
#Nesse exemplo temos uma impressão na tela da raiz quadrada de um número
#como queriamos apenas fazer essa funcionalidade, importamos apenas o que
#necessitava
print(raiz_quadrada(9))

