#Funçao decoradora utilizada para adiar 
#o funcionamento total de uma função
import os 

def checking(func):
    def check(*args, **kwargs):
        resultado = func(*args, **kwargs)
        os.system('cls')
        return resultado
    return check

@checking(sum)
def sum(x,y):
    return x+y

print(sum(1,2))