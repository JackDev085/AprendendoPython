import numpy as np
#Criando array bidimensional
data = np.random.randint(5, size=(3,3))
print(data)
"""

[[4 1 1]
 [4 2 3]
 [0 2 3]]
 """

#Atribuindo ao elemento na posicao [0,0] o valor 10
data[0,0] = 10

print(data)
"""
[[10  1  1]
 [ 4  2  3]
 [ 0  2  3]]
"""

#Elementos float quando adicionados a valores inteiros serão arrendonadados para inteiro
#para que não ocorra erros por parte do interpretador
data[1,1] = 11.5
print(data)
"""
[[10  1  3]
 [ 1 11  4]
 [ 3  3  2]]
"""

#Atribuindo um array para outro tipo
#Com o patametro dtype podemos atribuir a um numpy qualquer dado
data3 = np.array([8,-3,5,9], dtype ='float')
print(data3)#[ 8. -3.  5.  9.]
print(type(data3[0])) #<class 'numpy.float64'>