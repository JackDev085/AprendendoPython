from copy import deepcopy 
# Exercícios
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Aumente os preços dos produtos a seguir em 10%
copia_produtos = deepcopy(produtos)
for produto in copia_produtos:
    produto['preco']*=1.1.__round__(2)
# Gere novos_produtos por deep copy (cópia profunda)


# Ordene os produtos por nome decrescente (do maior para menor)
copia_produtos = sorted(copia_produtos, key=lambda x:x['nome'], reverse=True)

# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = deepcopy(sorted(copia_produtos, key=lambda x:x['nome']))

# Ordene os produtos por preco crescente (do menor para maior)
produtos_ordenados = sorted(copia_produtos, key=lambda x: x['preco'], reverse=True)


#Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = deepcopy(sorted(copia_produtos, key=lambda x:x['preco']))


for produto in produtos:
   print(produto)
print()
for produto in produtos_ordenados_por_preco:
    print(produto)