#Por meio da função filter() também realizaremos iterações sobre um #
#elemento de uma lista ou dicionário, porém usado de lógica condicional

#Via map() podemos realizar toda e qualquer iteração sobre um determinado
#elemento, enquanto via filter() literalmente filtraremos um determinado dado/valor
#de um elemento quando o mesmo respeitar uma certa condição imposta

#Lista de pessoas, contendo nome e idade
pessoas =[
    {"Nome":"Ana", "idade":32},
    {"Nome":"julia", "idade":42},
    {"Nome":"marcela", "idade":36},
    {"Nome":"joao", "idade":312},
    {"Nome":"cesa", "idade":62}
]
#Aqui estamos atribuindo a variável idoso um filter() que por sua vez parametriza uma
#expressão lamba que buscar todos os elementos que possuem idade maior que 60
idoso = filter(lambda x: x['idade'] >60 , pessoas)
#Apartir do filtro aqui será exibido o resultado da lista já com os valoes
#"separados"
print(list(idoso))


#=============================================================
#Criando um dicionário de produtos, com nome e preco
produtos =[
    {"Nome":"item 1", "preco":32},
    {"Nome":"item 2", "preco":42},
    {"Nome":"item 3", "preco":36},
    {"Nome":"item 4", "preco":312},
    {"Nome":"item 5", "preco":62}
]

#criação de uma função para filtrar elementos dada uma lista
#Nessa função tem uma condicional, nela se o produto tiver o elemento preco maior que 50
#retorna true

def filtra(p):
    if p['preco'] > 50:
        return True
#Temos uma variavel nova_lista 3 que recebe uma funcao filter() que parametriza a funcao filtra()
#na estrutura de dados  proutos ou seja o filtro irá analisar quais dos produtos tem preço mair que 50
#Sendo assim sera adicionado a nova_lista3 apenas os produtos mais expensivos que o valor de 50

nova_lista3 = filter(filtra, produtos)
#um for para mostrar os valores
for produtos1 in nova_lista3:
    print(produtos1)