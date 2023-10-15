#Basicamente raise pode ser usado sempre que quisermos levantar um erro
#ao qual já foi previso ou que é comumento possível de ocorrer. Neste contexto,
#geramos uma mensageme especifica para  erro
idade = int(input('Digite sua idade: '))

if idade <= 0:
    raise Exception ("Idade inválida")
print((f'Você tem {idade} anos'))