
#Lista de tupla
lista = [('valor1','valor2'), ('valor2', 'valor2'), ('valor3', 'valor3')]

#conversão de lista de tuplas para dict comprehension
dicionar = {x:y for x,y in lista}
print(dicionar)


#ex

'''Aqui temos um exemplo de uma lista de tuplas'''
produtos =[('caneta', 1.98), ('lapis' ,2.1), ('azulejo', 5.9)]
#aAqui estamos pegando a lista de tuplas e aplicando imposto a ela com comprehension
produtos_com_imposto ={x:y*1.6 for x,y in produtos}

print(produtos)
print(produtos_com_imposto)