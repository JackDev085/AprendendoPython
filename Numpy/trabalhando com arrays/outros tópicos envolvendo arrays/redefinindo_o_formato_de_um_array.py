import numpy as np

#criando um array unidimensional de 9 elementos ordenado
data = np.arange(8)
print(data)#[0 1 2 3 4 5 6 7]

#Mudando o array unidimensional para bidimensional 2x4 com o método reshape()
data = data.reshape(2,4)
print(data)#[[0 1 2 3]
           #4 5 6 7]]
