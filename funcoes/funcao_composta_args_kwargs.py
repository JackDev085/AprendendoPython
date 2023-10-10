"""args e kwargs são parametros de funcoes que sigficam lista ou
dicionários. São palavras reservadas mas também pode ser usado
qualquer palavra no seu lugar"""

# * = args (tratados como lista)
# ** = kwargs (tratados como dicionario)

#Funcao que printa na tela duas vezes algum parametro de texto
def print_2_vezes(*args):
    for parametro in args:
            print(parametro + '!' + parametro + '!')

print_2_vezes('É sobre isso!!! ', 'isso ai irmao')


#funcao para percorrer um dicionario e retornar itens 
def mostrar_dados(**kwarg):
      for dado, valor in kwarg.items():
            print(dado + ' - ' + str (valor))

pessoa = mostrar_dados(nome='juao',
                     idade= 12,
                     nacionalidade='brasileiro')
print(pessoa)
            