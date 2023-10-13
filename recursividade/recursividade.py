#Em alguns programas mais robustos as funções necessitam
#ser realizadas mais de uma vez. A recursividade pode ajudar
#nesse quesito

def fatorial(num:int) -> int:
    if num ==1:
        return 1
    #Aqyu temos a recursividade(Onde a função chama ela mesma
    #entretanto com um comportamento diferente)
    return num * fatorial(num - 1)

fator = fatorial(12)
print(fator)