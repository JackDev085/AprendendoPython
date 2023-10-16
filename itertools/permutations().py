from itertools import permutations

lista10 = ['ana' , 'bianca', 'julia', 'roberta']

#diferente das combination() o permutation exibe todas as combinações possiveis
#mesmo que haja repetições

#permutations rece uma lista e o número de combinações como parâmetro
for combinacoes in permutations(lista10, 2):
     print(combinacoes)
"""
('ana', 'bianca')
('ana', 'julia')
('ana', 'roberta')
('bianca', 'ana')
('bianca', 'julia')
('bianca', 'roberta')
('julia', 'ana')
('julia', 'bianca')
('julia', 'roberta')
('roberta', 'ana')
('roberta', 'bianca')
('roberta', 'julia')
"""