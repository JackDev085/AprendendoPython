import numpy as np

#a variável data rece uma função numpy
#A função np.random.randint() cria valores aleatórios até um certo parâmetro

#O primeiro parâmetro se dá pelo intervalo de numéros (nesse exemplo é dez, então será gerado números de 0 a 10)
#O segundo parâmetro se dá respeito a quandtidade de números a serem gerados
data = np.random.randint(10, size = 10)
print(data)#[3 3 4 8 6 2 0 0 7 7]