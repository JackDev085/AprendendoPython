class Vazia:
    pass#Quando  utilizo a palavra pass automaticamente a classe não cobra 
#que eu implemente os atributos e metodos a ela. Assumindo assim a responsabilidade para o dev

#Aqui implementamos uma instancia de classe e atribuimos valores a ela dinamicamente
vazia1 = Vazia()
vazia1.nome = 'jack'
vazia1.idade = 21

print(f'Nome: {vazia1.nome} Idade: {vazia1.idade}')
print(type(vazia1))