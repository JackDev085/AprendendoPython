from functools import reduce
estoque = [
    {'item1' : 'camisa nike', 'preco': 35.90},
    {'item2' : 'camisa adidas', 'preco': 37.20},
    {'item3' : 'moletom gg', 'preco': 70.40},
    {'item4' : 'calca jeans', 'preco': 60.10},
    {'item5' : 'tenis allstar', 'preco': 105.90}
]

#Método convencional para extrair dados

precos01 = []
for preco in estoque:
    precos01.append(preco['preco'])
print(f"Preeços do estoque (normal) {precos01}")

#EXTRAINDO DADOS VIA MAP + FUNCAO LAMBDA

precos02 = list(map(lambda p:p['preco'],estoque))
for preco in precos02:#Mostrando os preços
    print(preco)
print(f"Preeços do estoque (lambda) {precos02}")

#EXTRAINDO DADOS VIA LIST COMPREHENSION

precos03 = [preco['preco'] for preco in estoque]
print(f"Preeços do estoque (List Comprehension) {precos03}")

#EXTRAINDO DADOS VIA FILTER

precos04 = list(filter(lambda p:p['preco']>= 60, estoque))
print(f"Preeços do estoque (Filter) {precos04}")

#EXTRAINDO DADOS VIA REDUCE + LIST COMPREHENSION

'''Não muito diferente dos exemplos anteriores, trabalhando com Reduce
podemos perfeitamente usar de list comprehension dentro de nossas expressões
'''

'''Inicialmente é criada uma variável precos_total que recebe reduce() parametrizando
a mesma com uma expressão lambda que recebe soma ,valores e realiza a soma dos mesmos,
buscando dados de estoque e iniciando a soma em 0'''
precos_total = reduce(lambda soma, valores: soma+valores['preco'], estoque, 0)
print(f"Soma dos precos (Reduce + List Comprehension) {precos_total}")

#EXTRAINDO DADOS VIA REDUCE (MÉTODO OTIMIZADO)
precos_total = sum(['preco'] for preco in estoque)
print(f'Soma dos Preços (reduce metodo otimizado {precos_total}')