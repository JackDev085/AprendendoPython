import  numpy as np

#Aqui iremos gerar um array de 10 elementos com valores distribuidos entre 0 a 5
#com a função np.random.randint(intervalo_de_numeros, size=var_tamanho)
data = np.random.randint(5, size=10)
print(data)#[1 2 4 0 2 0 3 4 4 2]
print(data.shape)#(10,)