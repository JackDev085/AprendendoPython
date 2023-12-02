def une_listas(lista1, lista2):
    return [(lista1[i], lista2[i]) for i in range(min(len(lista1),len(lista2)))]

lista1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista2 = ['BA', 'SP', 'MG', 'RJ']
print(une_listas(lista1, lista2))