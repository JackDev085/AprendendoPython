from itertools import combinations


lista10 = ['ana' , 'bianca', 'julia', 'roberta']

#a função combinações faz jus ao nome. Ele recbe uma list como parâmetro e
#faz combinacoes entre si, a medida que as combinações vao acontecendo
#se tem uma diminuição nos número devido algumas combinações se repetirem
for combinacoes in combinations(lista10, 2):
     print(combinacoes)
'''
('ana', 'bianca')
('ana', 'julia')
('ana', 'roberta')
('bianca', 'julia')
('bianca', 'roberta')
('julia', 'roberta')
'''