# Variáveis livres + nonlocal (locals, globals)

# Em Python, a palavra-chave nonlocal é usada dentro de uma função para
# indicar que uma variável se refere a uma variável na função pai mais próxima 
# que não é global. Isso é útil quando você tem funções aninhadas (uma função 
# dentro de outra) e deseja modificar o valor
# de uma variável da função pai mais próxima que não é a função global.
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)