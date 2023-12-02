
try:
    a = 2
    b = 0
    c = a/b
except ZeroDivisionError as error:
    print('Erro' , error.__class__.__name__)