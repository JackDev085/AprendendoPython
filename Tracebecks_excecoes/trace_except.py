"""Tracebacks ou exceÇões podem ocorrer quando cometemos um erro de lógica ou
de sintaxe na execução do programa em questão.

Para resolver isso pode se criar execções personalizadas para informar
em que local ocorreu esse erro ou o que causou ele"""

#Ex de erro comum

var1 = 2
var2 = 'julia'

#Quando for executar o código e tentar imprimir o valor dessa soma vai 
#trazer uma exceção. Pois houve um erro de lógica
print(var1+var2)