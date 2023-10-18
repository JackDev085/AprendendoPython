import numpy as np
#Criando uma array ordenada de 10 elementos
data = np.arange(10)

#Imprimindo os elementos do array data
print(data)#[0 1 2 3 4 5 6 7 8 9]
#imprimindo os elementos em forma de booleano caso eles sejam maior que um valor que no caso desse exemplo 3
print(data >3)
print('==========================================================')
print(data)#[0 1 2 3 4 5 6 7 8 9]
#Imprimindo um booleano resultando a condição se o elemento da posição 4 do array é maior que 5
print(data[4]>5) #False
