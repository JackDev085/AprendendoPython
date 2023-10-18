#Criação de um array com dados/valores distribuidos de maneira uniforma na mesma
import numpy as np

#Por meio da função linspace() podemos criar dados uniformemente arranjados dentro de uma array
#Estamos gerando uma array composta de 7 elementos igualmente distribuidos, com valores entre 0 e 1
data = np.linspace(0,1,7)
print(data)