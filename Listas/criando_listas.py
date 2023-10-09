#iniciando lista vazia
lista=[]

#iniciando lista com valores mesclados
lista2= [1 , 2 , 'maria' , 5]

#Adicionando um valor a lista (.append(obj))
lista2.append('1')
print(lista2)

#Removendo um dado na lista(.remove(obj))
lista2.remove('maria')
print(lista2)

#Removendo um dado na lista apartir do indice(del lista[indice])
del lista2[1]
print(lista2)

#Verificando a posição de um elemnto(.index(obj))
print(lista2.index(5))

#Verificando se um elemento está na lista('obj' in lista)
print(5 in lista2)#retorna true se o elemento estiver na lista
print('=======================')
#Invertendo dados de uma lista
lista3 = ['joao' , 'maria']

lista3.reverse()
print(lista3)
