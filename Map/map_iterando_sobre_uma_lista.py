#Exemplo de uso do map()

#criação de uma lsita
lista = [1,2,3,4,5,6,7,8,9,10]
#atribuindo a nova_lista uma função map() que utiliza uma expressão lamba
#que multiplica todos os elementos da lista por 2
nova_lista = map(lambda x: x*2, lista)

#Mesmo exemplo, no entanto usando o list comprehension
nova_lista1 = [ x * 2 for x in lista ]

print(lista)
print(list(nova_lista))
print(nova_lista1)

"""1 - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2 - [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
3 - [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]"""

#Com o uso da função map() temos uma melhor performance a
#rodar o programa