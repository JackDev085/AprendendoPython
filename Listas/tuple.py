#Tuple é uma estruturado de dados estática


#Para que o interpretador não se confunda, achando que é um simples objeto
#com um parãmetro atribuido, pela sintaxe, mesmo qe haja só um elemento na tupla
#deve have ao menos uma vigula como separador.
minhaTupla = tuple()
minhaTupla = (1,2,3)

print(minhaTupla[0])

cores = tuple()
cores = ('azul' ,'branco' ,'vermelho' , 'rosa',
               'azul', 'verde' , 'azul')

#Método Count usado para contar quantos elementos se repetem
print(cores.count('azul'))