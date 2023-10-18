import numpy as np
#criando variavel
tamanho = 10

#por meio da funcao np.random.permutation() podemos definir um tamanho que pode
#ser modificado conforme a necessidade


data = np.random.permutation(tamanho)
print(data)#[4 8 5 3 6 1 2 7 0 9]