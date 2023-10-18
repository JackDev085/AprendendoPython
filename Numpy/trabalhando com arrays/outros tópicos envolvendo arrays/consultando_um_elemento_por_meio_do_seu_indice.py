#ARRAY UNIDIMENSIONAL
import numpy as np

#Criando array ordenado de 15 elementos
data = np.arange(15)

print(data) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
#Aqui mostramos no array qual elemento está na posição 8
print(data[8]) #8
#Caso seja passado uma opsição de valor negativa será exibido o respectivo elemento a conta
#do final para o começo do array
print(data[-5]) #10

#ARRAY BIDIMENSIONAL

#Criando array bidimensional de valores aleatórios
data2 = np.random.randint(5, size= (3,4))

print(data2)
'''
[[3 3 3 4]
 [2 0 3 4]
 [1 3 3 2]]
 '''
print(data2[0,2])#3
'''
[[3 3 '3' 4]
 [2 0 3 4]
 [1 3 3 2]]
 '''