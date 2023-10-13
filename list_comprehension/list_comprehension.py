# Com a chegada do python 3 as formas de manipular dados foram se aprimorando

#Forma mais utilizado pelos novos estudantes de python para
#percorrer uma lista
lista1 = [1,2,3,4,5]
for i in lista1:
    print(i*2)

#Otimizaando nosso código, repare que temos exatamente a mesma lista
#porémm aagora criamos uma nova variável de nome lista2, que rcebe
#como atributo uma list comprehension realizando a mesma funcao do exemplo
#anterior, porém de forma reduzida e otimizada via list comprehension
lista2 = [1,2,3,4,5]
lista3 = [i*2 for i in lista2]
print(lista3)