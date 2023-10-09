#Analisando se um conjunto pertence a outro conjunto

#Criando dois conjuntos
c1 = {1,2,}
c2 = {2,3}
#união entre conjuntos
c1.union(c2)
#atualizando o conjunto com a união
c1.update(c2)
#se os valores de c2 estiverem contidos em c1 ele pertencerá ao conjunto 
print(c2 <= c1)