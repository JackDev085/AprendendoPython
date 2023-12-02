
lista = [1,2,3,4,5,6]
suave = list(map(lambda x: x*2, lista))
for suav in suave:
    print(suav)


lista_filtrada =list(filter(lambda x: x > 2, lista ))
print(lista_filtrada)