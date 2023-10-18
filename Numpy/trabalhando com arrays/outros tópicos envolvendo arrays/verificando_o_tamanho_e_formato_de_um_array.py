import numpy as np

data = np.random.randint(5, size=(5,3,4))
#Retora o número de dimensões
print(data.ndim)
#3

#retorna o formato de nossa array(formato de cada dimensão da mesma)
print(data.shape)
#(5, 3, 4)

#retorna o tamanho total dessa matriz
print(data.size)
#60