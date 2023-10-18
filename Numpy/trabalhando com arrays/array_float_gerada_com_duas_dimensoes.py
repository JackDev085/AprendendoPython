import numpy as np

#Podemos via np.random.random() gerar arrays de dados tipo float, no intervalo entre 0 e 1
#aqui com mais de uma dimensão. Note que para isso é necessário colocar o número de linhas e colunas
#dentro de um segundo par de parênteses
data = np.random.random((2,2))
print(data)##[[0.55708635 0.65596452]
            #[0.04608498 0.7089717 ]]