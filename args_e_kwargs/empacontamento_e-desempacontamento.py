#Aqui temos exemplo de uma tupla e um dicionário respectivamente

numeros = (33,1987, 2920,121,12.9)
dados = {'Nome':'Fernando', 'Profissão':'professor'}

#aqui uma função que tem como parametro um dado do "tipo" args e 0utro do "tipo" kwargs
def identificadores(*args, **kwargs):
    print(args)
    print(kwargs)

identificadores(*numeros, **dados)