#Declarando lista
lista= [1,2,3,'paulo']
print(lista)
#Adicionando uma lista dentro de uma lista manualmente
lista =[1, 2 , 3 , 'paulo', [2, 'maria', 'jose']] 
print(lista)
#Criando uma segunda lista
lista2 = [1, 5, 6, 4]
#Adicionando uma lista em outra lista utilizando o mtodo .append(list)
lista.append(lista2)
print (lista)