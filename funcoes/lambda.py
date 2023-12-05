#Funcoes lambda, são nada mais que funcoes simples
#que realizam tarefas simples. Normalmente
#associadas a uma variável de forma que sua função
'''é executada apenas naquele bloco de código sem ser por padrão reutilizávei'''

#aqui temos uma variável que recebe uma função lambda
#a expressão e variáveis são separados por ":"
variavel1 = lambda n1, n2 : n1*n2#Note que a ação dessa função é uma multiplicação
#entre as variáveis n1 e n2
n1= 2
n2 = 3
print(variavel1(n1,n2))

#agora vamos mostrar um exemplo de multiplicação padrão

def multiplica(n1,n2):
    resultMulti = n1*n2
    print(resultMulti)
multiplica(n1,n2)