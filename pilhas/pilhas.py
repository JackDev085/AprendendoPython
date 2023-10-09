#Pilhas são estruturas de dados em que sua adição e remoção 
#acontecem por suas extremidades( ex pilha de pratos)
pilha = [10,20,30]

#Adicionando um elemento ao final da pilha pilha.append(elemento)
pilha.append(50)
print(pilha)

print('================')

#Removendo elemento de uma pilha
pilha2 = [10,20,30]
pilha2.pop()
print(pilha2)

print('================')
#Consultando o tamanho da pilha
pilha3 = [10,20,30]
pilha3.append(50)

print(len(pilha3))