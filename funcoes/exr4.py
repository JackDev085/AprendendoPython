nomes = ['joao','joana','julio','marcelo']

nome_list = []

for nome1 in nomes:
    for nome2 in nomes:
        if nome1+nome2 in nome_list or nome1+nome1 in nome_list or nome2+nome2 in nome_list or nome2+nome1 in nome_list:
            continue
        if nome1+nome2 in nome_list:
            continue
        else:
            nome_list.append(nome1+nome2)
            
print(nome_list)
            
            
            
a =5
b = 2.5

c = a+b

print(c)