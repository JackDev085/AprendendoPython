"""
No Python, os dicionários são coleções de itens
desordenados com uma diferença bem grande quando
comparados às outras coleções (lists, sets, tuples, etc)
:um elemento dentro de um dicionário possui uma chave
 atrelada a ele, uma espécie de identificador. Sendo assim,
 é muito utilizado quando queremos armazenar dados de forma
  organizada e que possuem identificação única (como acontece
   em bancos de dados).
"""

#Existem duas formas de se criar um dicionário utilizando
# o Python. A primeira delas é utilizando chaves ( {} )
# e separando os elementos das chaves com dois pontos ( : )
# e os outros elementos por vírgula ( , ):

dicionario = {1: 'joao', 2:'silva'}
dicionario = {'nome’: ‘João’, ‘sobrenome':'silva'}

#A segunda forma é utilizando o método dict() com o dicionário sendo passado como parâmetro:


nome_do_dicionario = dict({1:'joao', 2:'silva'})
nome_do_dicionario = dict({'nome':'joao', "Sobrenome": "Silva"})