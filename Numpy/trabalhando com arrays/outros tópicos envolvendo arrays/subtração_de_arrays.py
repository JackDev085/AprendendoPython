import numpy as np


#è possivel fazer a subtração de arrays seguindo a lógica que os dois array necessitam ter o mesmo número de elementos

d1 = np.array([3,6,3,12,0,2])
d2 = np.array([2,4,1,8,1,2])

d3 = d1 - d2
print(d3)#[ 1  2  2  4 -1  0]