##realizando uma conversão de um array multidimensional para unidimensional, de modo que
#se mantenha a indexação interna da mesma para que possa ser posteriormente convertida novamente para seu formato original
import numpy as np

#é isso que é feito por meia da fução flatten()

data = np.array([(1,2,3,4) , (1,2,3,4)])
print(data)
#[[1 2 3 4]
#[1 2 3 4]]
data_flat = data.flatten()
print(data_flat)#[1 2 3 4 1 2 3 4]
