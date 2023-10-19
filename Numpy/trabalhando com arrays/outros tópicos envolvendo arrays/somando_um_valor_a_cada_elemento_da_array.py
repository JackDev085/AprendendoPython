#a partir do momento que uma matriz passa a ser uma array do tipo numpy é possivel reaalizar tais operações
#desde que leve em conseideração que a operação realiada se aplicará a cada um dos elementos da array

import numpy as np

data = np.arange(0,15)
print(data)#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

data = np.arange(0,15) +1
print(data)#[ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15]

data = np.arange(0,30,3)+3
print(data)#[ 3  6  9 12 15 18 21 24 27 30]