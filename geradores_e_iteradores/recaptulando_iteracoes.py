#Um objeto iterável é aquele tipo de objeto ao qual podemos
#interagir com seus elementos, cada elemento de sua compósição

minha_lista = [1,2,3,4]

#Por meio da função hashttr() podemos verifcar se internamente minha_lista
#possui o método __iter__
print(hasattr(minha_lista, '__iter__'))
#todo objeto iterável em python internamente possui em sua comoposição o método __iter__
#como um sinalizado que o interpretador permita o instanciamento e uso de todo e qualquer dado
#deste objeto
for i in minha_lista:
    print(i)

