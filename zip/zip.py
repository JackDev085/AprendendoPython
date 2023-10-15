##Manipulação de listas com zip()
#Essa funcção realiza a união de duas listas com equivalência de elementos
# e esse método ainda é menos propícia a exceções

cidades = ['porto alegre', 'curitiba', 'salvador', 'belo horizonte']
estados = ['RS', 'PR', 'BH', 'MG']

cidades_estados = zip(cidades,estados)

for i in cidades_estados:
    print(i)#Resutado do for abaixo:
'''('porto alegre', 'RS')
('curitiba', 'PR')
('salvador', 'BH')
('belo horizonte', 'MG')
'''
