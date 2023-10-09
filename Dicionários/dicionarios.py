#Dicionários são estruturas de dados do tipo chave:valor

#Dicionario com um veiculo e seu respectivo local para uso
dicionario = {'aviao':'ceu', 'carro':'terra','moto':'terra',
'barco':'mar'}

print(dicionario['carro'])

#Dicioário para um fucionário
funcionario = { 'nome':'fernando',
                'idade':22,
                'funcao':'faxineiro',
                'moradia':'rua 15 123',
                'formacao':['educacao fisica', 'saude']}
print(funcionario)
print(len(funcionario))

#Visualizando quais são as chaves de um dicionario dicionario.keys()

print(funcionario.keys())
print('===================================')
#Mostrando todas as chaves e valores de um dicionario mais organizado (dict.items())
print(funcionario.items())

print('===================================')
#Alterando o dados de um valor com uma chave. dicionario[chave] = valor

funcionario['formacao']=['servicos-gerais', 'limpeza']
print(funcionario.items())

#Adicionando mais um valor em uma chave no dicionario
print('===================================')
funcionario['formacao'].append('Especialização em pesca')
print(funcionario.items())