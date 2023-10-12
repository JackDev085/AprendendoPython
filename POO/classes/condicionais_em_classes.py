#Criando classe que pode ser idealizada como "rede social"
class Social:
    #Criando método sem parametro e com 2 parâmetros sem obrigatoriedade
    def __init__(self ,nome, login=False, logoof=False ):
        self.nome = nome
        self.login = login
        self.logoof = logoof

    #Método para logar um usuário que receberá como parâmetro um objeto do construtor
    def logar(self):
        #Estrutura condicional que executará caso o atributo
        # "loguin" seja igual a Verdadiro
        if self.login:
            print(self.nome+ ' Você está logado')
            return
        #Logando o usuário e mudando o atributo loguin para true
        print(f'Você acabou de entrar na rede {self.nome}')
        self.login = True

        #Método para deslogar o usuario do sistema
    def deslogar(self):
        if not self.login:
            print('O usuário não está logado no sistema')
            return

        print('O usuário foi deslogado do sistema')
        self.login = False
#criando o objeto
pessoa1 = Social('jack')

#logando o objeto
pessoa1.logar()
pessoa1.logar()
#Deslogando o objeto
pessoa1.deslogar()
pessoa1.deslogar()