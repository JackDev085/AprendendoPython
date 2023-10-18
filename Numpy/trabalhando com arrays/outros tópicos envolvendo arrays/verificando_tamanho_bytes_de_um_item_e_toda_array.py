import numpy as np
#criando uma array unidimensional
data= np.random.randint(5, size=10)
print(data)

#Aqui mostramos o tamanho em bytes de cada item da array
print(f'Cada elemento possui {data.itemsize} bytes ')
#Aqui mostramos o tamanho em bytes de cada item da array
print(f'toda a matriz possui {data.nbytes} bytes ')