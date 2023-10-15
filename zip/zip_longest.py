#A função zip funciona bem quando temos duas lista com tamanho iguais
#Quando temos listas com tamanhos diferentes podemo usar a função zip_longest()

#para isso temos que importar essa função da biblioteca itertools
from itertools import zip_longest

#Criando duas listas de cidades e estados
cidades = ['porto alegre', 'curitiba','salvador','belo horizonte', 'rio de janeiro', 'goiânia']
estados =['RS', 'PR', 'BH', 'MG']

#Aqui estamos atribuindo a variável cidades_estados a função zip_longest() fazendo a união
#de duas listas de valores diferentes, e os valores que não tiverem pares, estará adicionando ao seu segundo
#elemento de tupla um resultado: none
cidades_estados = zip_longest(cidades,estados)

#Já aqui fazemos a mesma coisa da primeira função entretanto os resulados que não houverem pares
#Será adicionado a variável o 3 parãmetro que está adicionado ao declarar da lista: "Desconhecido"
cidades_estados2 = zip_longest(cidades,estados, fillvalue='Desconhecido')

#Aqui temos um comprehension sendo atribuido a uma variável
resposta = {x:y for x,y in cidades_estados}
resposta2 = {x:y for x,y in cidades_estados2}

print((resposta))
print((resposta2))