#Afim de trazer um entendimento mais fácil aqui temo um exemplo

#Esse exemplo retrata compras e os items sendo somados for alocando
#o valor total dentro do for
carrinho = []
carrinho.append(('item1',30))
carrinho.append(('item2',10))
carrinho.append(('item3',20))
total = 0

for produto in carrinho:
    total = total + produto[1]
print('Método tradicional', total)#Método tradicional 60

#Já aqui temos um código mais enxuto e performático
#Definição de uma lista
total2= []

#for para percorre os produtos n carrinnho
for produto in carrinho:
    total2.append(produto[1]) #adicionando todos os valores de produtos
    #na variavel total2
print('Usando função interna',sum(total2))#Usando função interna 60

#Aprimorando mais ainda o código, o mesmo pode ser reescrito utilizando
#list comprhension






carrinho = []
carrinho.append(('item1',30))
carrinho.append(('item2',10))
carrinho.append(('item3',20))
total = 0

for produto in carrinho:
    total = total + produto[1]
print('Método tradicional', total)#Método tradicional 60

total3 = sum([y for x,y in carrinho])
print('Usando list comprehension',total3)