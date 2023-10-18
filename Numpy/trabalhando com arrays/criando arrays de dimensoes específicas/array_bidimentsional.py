import  numpy as np

#Estamos atribuindo a data uma função np.random.int() que recebe um intervalo de elementos com parametro e um size
#que por sua vez se delimita como um tamanho de 3x4. ou 3 linhas e 4 colunas, gerando valores aleatórios no intervalo de 0 a 5
data = np.random.randint(5 , size=(3,4))
print(data)#[[3 0 2 1]
            #[1 1 2 3]
            #[4 0 4 1]]
print(data.shape)#(3,4)