import  numpy as np

#Estamos atribuindo a data uma função np.random.int() que recebe um intervalo de elementos com parametro e um size

#o número definido para size, agora com 3 parâmetros, estamos definindo um array de formato tridimensional

#Nesse caso, importante entender que dos três parâmetros se refere ao número de camadas que a array terá em sua terceira dimensão
#enquanto o segundo paarâmetro define o número de linhas e o terceiro parâmetro o numero de colunas
data = np.random.randint(5 , size=(5,3,4))
print(data)
'''
[[[0 0 1 2]
  [2 2 1 0]
  [2 0 2 1]]

 [[1 1 2 2]
  [3 1 2 0]
  [2 4 0 2]]

 [[1 2 1 2]
  [1 4 1 4]
  [2 4 0 0]]

 [[1 1 0 3]
  [4 4 2 3]
  [4 3 3 3]]

 [[2 0 4 0]
  [3 2 2 1]
  [3 1 3 0]]]
  '''
print(data.shape)#(5,3,4)