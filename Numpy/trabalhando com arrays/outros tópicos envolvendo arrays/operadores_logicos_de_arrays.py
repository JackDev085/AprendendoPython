import numpy as np


#è possivel utilizar operadores lógicos em arrays seguindo a lógica que os dois array necessitam ter o mesmo número de elementos

d1 = np.array([3,6,3,6,1,2])
d2 = np.array([5,6,4,9,12,2])

d3 = d2>d1
print(d3)#[ True False  True  True  True False]