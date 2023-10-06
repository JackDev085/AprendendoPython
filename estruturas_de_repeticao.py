#Estruturas que realizam trechos de código 
#até que uma condição for válida

#While = enquanto ( Geralmente usado quando não sabemos quantas vezes queremos executar um código)

a = 1

while a < 8: #Enquanto a for menor que 8 mostrará na tela o valor de A e acrescetará 1 a seu valor
    print(a)
    a += 1 #Incremento


    #===============================================================================  


#For = para (Geralmente usado quando sabemos quantas vezes queremos executar um código)

compras = {'arroz','macarrão', 'feijão','frango'}

for i in compras: #Semelheante ao FOR EACH. Nesse trecho de código realiza-se uma procura por itens 
    print(i)#na lista compras, para cada objeto i de compras será imprimido i.
   

for x in range(0,6): #Aqui temos um for com um número de repetições pré determinada, a palavra reservada
    print(f'Número {x}') #'range'(início,fim) determina quantas vezes esse código será executado. 
    

nomes = {'jõao' ,'julia', 'bernardo'}
for x in nomes: #Como o for é testado uma condição (Tipo if) podemos adicionar a ele um
    print(x) #Else e caso não seja atestada uma condição partir para o seu uso
else:
    print("Cabou a lista")



    #Imprimindo a tabuáda com PYTHON

    for z in range(12):
        for w in range(12):
            print(f'{z} X {w} = { z * w }' )