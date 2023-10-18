import numpy as np

data = np.arange(15)

#Impressão normal dos elementos da var data
print(data) #[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
#Impressão dos elementos anteriores ao parâmetro
print(data[:5]) #[0 1 2 3 4] - mesmo que data[0:5}
#impressão dos elementos do terceiro em diante todos os demais
print(data[3:])#[ 3  4  5  6  7  8  9 10 11 12 13 14] - mesmo que data[3:final_do_array}
#Estaremos exibindo do quarto elemento em diante
print(data[4:8])#[4 5 6 7]
#Exibe de dois em dois elementos, todos os elementos.
print(data[::2])
#Estamos pulando os 3 primeiros elementos e exibindo todos os demais
print(data[3::])#[ 3  4  5  6  7  8  9 10 11 12 13 14]


