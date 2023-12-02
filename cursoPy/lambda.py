lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
 ]


# lista.sort(key=lambda item:item['nome'])

# for item in lista:
#     print(item)
def executa(funcao,*args):
    return funcao(*args)

duplica=(
    executa(
        lambda x: lambda y: x*y,
        10
        )
)
print(duplica(2))