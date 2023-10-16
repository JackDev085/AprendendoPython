from itertools import product
lista10 = ['ana' , 'bianca', 'julia', 'roberta']

#Nesse exemplo temos combinações entre os itens da lista inclusive o próprio item.

#a função product() recebe uma lista e um repeat = x(vezes que irá combinar os elementos)
for combinacoes in product(lista10,repeat = 2):
     print(combinacoes)

"""
('ana', 'ana')
('ana', 'bianca')
('ana', 'julia')
('ana', 'roberta')
('bianca', 'ana')
('bianca', 'bianca')
('bianca', 'julia')
('bianca', 'roberta')
('julia', 'ana')
('julia', 'bianca')
('julia', 'julia')
('julia', 'roberta')
('roberta', 'ana')
('roberta', 'bianca')
('roberta', 'julia')
('roberta', 'roberta')
"""