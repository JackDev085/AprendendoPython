import numpy as np

#Dependendo da aplicação, pode ser necessário gerar arrays numpy previamente preenchidas com um tipo de dado específico.
#Em machine learning, por exemplo ,existem várias aplicações onde se cria uma matriz
#inicialmente com valores ''1'' a serem substituidos apos algumas funções serem executada e gerarem retornos

#Por meio da função np.ones(()) podemos criar um array com as dimensões que quisermos, totalmente preenchida com números 1.
#Nesse caso, um array com 3 linhas e 4 colunas devrá ser gerada
data= np.ones((3,4))
print(data)#[[1. 1. 1. 1.]
           #[1. 1. 1. 1.]
           #[1. 1. 1. 1.]]
