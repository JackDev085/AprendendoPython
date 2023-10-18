import numpy as np

data = np.diag((1,2,3,4,5,6,7,8))
print(data)

#aqui temos uma matrix 8x8 com a diagonal sendo prenchida pela ordenação do 1 até o 8
'''[[1 0 0 0 0 0 0 0]
 [0 2 0 0 0 0 0 0]
 [0 0 3 0 0 0 0 0]
 [0 0 0 4 0 0 0 0]
 [0 0 0 0 5 0 0 0]
 [0 0 0 0 0 6 0 0]
 [0 0 0 0 0 0 7 0]
 [0 0 0 0 0 0 0 8]]
'''
#Cria uma matriz diagonal com vlaores 0 a 1,  de tamanho definido pelo parâmetro repassado
#para função

#NEste caso, para a variavel data esta sendo criada uma array diagonal de 4 linhas
#e colunas conforme a parametrização realizada em np.eye()
data = np.eye(4)
print(data)
 #[[1. 0. 0. 0.]
 #[0. 1. 0. 0.]
 #[0. 0. 1. 0.]
 #[0. 0. 0. 1.]]
