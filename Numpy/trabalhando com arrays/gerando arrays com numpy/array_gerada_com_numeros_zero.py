import numpy as np

#Dependendo da aplicação, pode ser necessário gerar arrays numpy previamente preenchidas com um tipo de dado específico.
#Em machine learning, por exemplo ,existem várias aplicações onde se cria uma matriz
#inicialmente com valores zerados a serem substituidos apos algumas funções serem executada e gerarem retornos

#Por meio da função np.zeros() podemos criar um array com as dimensões que quisermos, totalmente preenchida com números 0.
#Nesse caso, um array com 3 linhas e 4 colunas devrá ser gerada
data= np.zeros((3,4))
print(data)#[[0. 0. 0. 0.]
           #[0. 0. 0. 0.]
           #[0. 0. 0. 0.]]
