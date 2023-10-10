#Recursividade é o termo usado para quando uma ação chama a ela mesma
'''Pode ser usada com funções que necessitam ser testadas varias vezes
até atender a uma condição.
Ex abaixo:'''

#criação de uma função que recebe dois valores como paramentro
def imprimir(maximo, atual):
    #condicao para atestar se um dos valores é igual ao valor maior
    if atual <= maximo:
        print(atual)
        #recursividade da função
        imprimir(maximo, atual+1)

imprimir(10, 1)