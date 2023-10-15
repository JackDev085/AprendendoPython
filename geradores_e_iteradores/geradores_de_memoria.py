import sys
#Instanciando 3 listas
lista_manual = list([0,1,2,3,4,5,6,7,8,9,10])
lista_gerada = list(range(10))
lista_milhao = list(range(1000001))

#Aqui podemos notar que a lista gerada tem uma performance maior , em comparação com a
#lista manual
print ("tamanho em bytes", sys.getsizeof(lista_manual))
print ("tamanho em bytes",sys.getsizeof(lista_gerada))
print ("tamanho em bytes",sys.getsizeof(lista_milhao))