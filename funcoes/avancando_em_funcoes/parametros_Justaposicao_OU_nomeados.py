#Quando criamo uma função em python temos que ter a cieência de que
#apartir que vamos adicionando os parametros necessários, temos
#que sequeniálos, pois o interpretador trabalha dessa maneira

class Pessoa():
    #                   1*      2*      3*
    def pessoaCadastro(nome , idade, funcao):
        nome = nome
        idade = idade
        funcao = funcao

#podemos também inicializar algum valor quando realizamos nossa
# a criação da nossa funcção por exemplo.

#isso é chamado de parâmetros nomeados

class Spotfy():
    def novoCadastro(nome, idade, plano ='basico' ):
        print(f'{nome}, com idade: {idade} plano: {plano}')