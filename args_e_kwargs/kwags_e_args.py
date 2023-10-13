#*args e **kwars são usados quando não sabemos quantos
#parametros iremos colocar em nossa funcao
def msg(nome, *args):
    print(f'{nome} = {args}')

ex1 = msg('fernando')
ex2 = msg('fernando', 'idade:21','funcao = técnico')

print(ex1)
print(ex2)



