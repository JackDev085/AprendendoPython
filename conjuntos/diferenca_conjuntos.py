#Difernça entre conjuntos = usado para ver os elementos que 
#que não se repetem nos dois cojuntos


#Criando dois conjuntos
c1 = {1,2}
c2 = {2,3}

c1.union(c2)
c1.update(c2)

c1 -= {2}
print(c1)