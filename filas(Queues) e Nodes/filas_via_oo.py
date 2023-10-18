#Any é uma estrutura de dado que pode ser inserida em qualquer contexto,
#guardando o lugar de algum tipo de dado que venha a substitur
from typing import Any

#Criando uma variável equivalente a uma constante, com a simples função de atribuir allgum dado
#onde possa não existir, evitando erros de interpretação
EMPTY_NODE_VALUE ='__EMPTY_NODE_VALUE__'

#Classe erro, será usada para levantar uma exceção via parãmetro Excetpion
#evia que o programa para de funcionar em funçã de um erro de interpretação
class Erro(Exception):
    ...
class Node:
    #Aqui é criado um construtor que recebe um valor qualquer como parametro
    def __init__(self, value, Any) ->None:
        self.value = value
        self.next = Node
        #aqui temos um método chamado __repr__() que retorna um valor em forma de string,simplesmente para que se possa
        #realizar a leitura do dado/valor atribuido a value
    def __repr__(self) -> str:
        return f'{self.value}'

    #Esse método deve retornar um valor True quando o valor de value for diferente de EMPTY_NODE_VALUE
    #o que em outras palavras nos diz que value não está mais em seu estado inical vazio, possuindo agora dados atribuidos a si
    def __bool__(self) -> bool:
        return bool(self.value != EMPTY_NODE_VALUE)
    #Aqui estamos criando a classe Queue onde irá alocar nossos dados
class Queue:
    #Aqui abaixo temos o método construturo que chama nossa classe Node parametrizando a mesma com EMPTY_NODE_VALUE. Em outras
    #palavras, aqui definimos uma posição inicial e uma final da fila, inicialmente vazias.
    def __init__(self) -> None:
        self.first: Node = Node(EMPTY_NODE_VALUE)
        self.last: Node = Node(EMPTY_NODE_VALUE)
        #Aqui foi criado um contador para saber quantos elementos essa fila possui
        self._count = 0

        #Função enqueue será responsável por adicionar elementos na fila e gerenciar a mesma
        #na sequência lógica esperada
    def enqueue(self , node_value:Any) -> None:
        novo_node = Node(node_value)
        #Caso não tenha um elemento na primeira posição será criado um novo node
        if not self.first:
            self.first = novo_node
        # Caso não tenha um elemento na última posição será criado um novo node
        if not self.last:
            self.last = novo_node
            #caso tenha tanto o primeiro elemento como o último será criado
            #um novo node e atribuido a primeira e última posição
        else:
            self.last.next = novo_node
            self.last = novo_node
        self._count += 1
    def pop(self) -> None:
        if not self.first:
            raise Erro('Sem elementos na fila')
        first = self.first

        if hasattr(self.first, 'next'):
            self.first = self.first.next
        else:
            self.firts = Node(EMPTY_NODE_VALUE)
        self._count =+1
        return
    def pook(self) -> Node:
        return self.firts
    def __len__(self) -> int:
        return - self._count
    def __bool__(self) ->bool:
        return bool(self._count)
    def __iter__(self) ->Queue:
        return self

    def __next__(self) -> Any:
        try:
            next_value = self.pop()
            return next_value
        except Erro:
            raise StopIteration