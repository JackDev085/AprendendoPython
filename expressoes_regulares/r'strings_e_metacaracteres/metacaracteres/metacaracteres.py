"""O metacaractre ponto(".") é usado em casos onde estaremos
realizando a leitura de uma string simples, normalmente
uma palavra, onde um determinado cartere
pode ser representado por vários elementos alterando seu contexto"""

#Importando biblioteca para usar metacarectere
import re

#criando uma variável para armazenar o texto
minha_string = 'Fernando chegará a meia noite.'
"""Onde estiver o simbolo '.' será buscado no texto o que o completa"""
print(re.findall(r'Fernand.', minha_string))

#Agora vamos fazer uma busca dupla utilizando o caractere
#'|' = "ou". Agora vamos buscar duas variações do mesmo nome
#para saber qual dos dois nomes está dentro da variável de texto
minha_string1 = 'Fernando chegará meio dia.'
print(re.findall(r'Fernando|Fernanda', minha_string1))

#Agora vamos para um exemplo mais elaborado,vamos usar um texto

texto1 = ('No dia trinta de março de dois mil e vinte foi inaugurado'
          'o novo ginásio de esportes da escola estadual Professor Annes Dias, na cidade de '
          'Cruz Alta, no estado do Rio Grande do Sul. A obra inciialmente '
          'crçada em um milhão de reai acabou não utilizando de todo o recurso,'
          'uma vez que dois grandes empresários da cidade, João Fagundes e Maria Terres doaram juntos'
          'em torno de duzentos mil reais. João Fagundes se manifestou dizendo que apoiou a obra pois acredita no desenvolvimento'
          'da cidade, assim investe regularmente para hospitais'
          'e escolas da mesma . Maria Terres não quis se pronunciar'
          'sobre o asunto.')
print(re.findall(r'.oão', texto1)) #primeiramente vamos buscar por esse texto .oão caso tenha alguma palavra contida
#que chegue perto irá completar e mostrar
print(re.findall(r'.oão | .aria', texto1))#aqui temos duas palavras ".oão" e ".aia"
#esse método irá buscar as palvras que completam essas senteças

#Outro simbolo que podemos usar é o "[]" para colocar mais de um parãmetro para procura
print(re.findall(r'[Jj]oão| .aria', texto1))
print(re.findall(r'[a-z]oão | [A-Z]oão',texto1))
print(re.findall(r'[a-zA-Z]oão',texto1))

'''Em certos casos podemos nos deparar com strings totalmente desconfiguradas
qunato a seus caracteres estarem em letra maiúsculas ou minuscúlas de forma aleatória
Nesses casos é possivel atribuiir um terceiro parãmetro para 
findall() chamado flags que é definido como re.I, em outras palavras,
essa sinalização para função findall() faz com que a mesma ignore o formato
dos caracteres e os leia normalmente'''
print(re.findall(r'JoÃo | MaRiA',texto1,flags=re.I))