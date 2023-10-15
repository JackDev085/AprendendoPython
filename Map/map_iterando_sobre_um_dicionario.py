#criacao de um dicionário

produtos =[
    {"Nome":"item 1", "preco":32},
    {"Nome":"item 2", "preco":42},
    {"Nome":"item 3", "preco":36},
    {"Nome":"item 4", "preco":312},
    {"Nome":"item 5", "preco":62}
]
#Aqui temos uma funcao map() por onde na expressao lambda percorre todos os valores do dicionario onde
#sua chave tem o nome de preco em produtos
precos = map(lambda p: p['preco'] ,produtos)
#Aqui estamos apenas exibindo os valores
for preco in precos:
    print(preco)

#==============================================
    #Outra prática comum, também visando performace, éa a de parametrizar a mesma com
    #Uma função independente.

    #criando uma função para aumentar o preço de todos os items na lista
def aumenta_precos(p):
    p['preco'] = p['preco'] * 1.05
    return p

#Preco2 rebeebe a funcao map() parametrizando a mesma com a variável aumenta)precos e com a variável
#onde os dados serão lidos, neste caso, produtos
preco2 = map(aumenta_precos, produtos)

#por fim um laço for para exibir os valores
for produto in preco2:
    print((produto))