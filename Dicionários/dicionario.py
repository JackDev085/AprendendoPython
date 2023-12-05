import os
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
i =0
for value in perguntas:
    print(f'{50 * "="}')
    print("Jogo da adivinhação")
    print(f'{50 * "="}')
    
    print(perguntas[i].get("Pergunta"))
    print(f'0) {perguntas[i].get("Opções")[0]}')
    print(f'1) {perguntas[i].get("Opções")[1]}')
    print(f'2) {perguntas[i].get("Opções")[2]}')
    print(f'3) {perguntas[i].get("Opções")[3]}')


    entrada = input("Qual o valor da pergunta? ")
    
    if  perguntas[i].get("Opções")[int(entrada)] == perguntas[i].get("Resposta"):
        print("Você acertou")
        i+=1
    else:
        print("Você errou")
        i+=1
    proxima_pergunta = str(input("Próxima pergunta? [Y] or [N]"))
    os.system('cls')
    if proxima_pergunta.upper() == 'Y':
        continue
        
    else:
        break
    

          




          
# print(f'{50 * '='}')
# print("Bem vindo ao jogo de adivinhação")
# print(f'{50 * '='}')
# pergunta1 = perguntas[0].get("Pergunta")
# opcoes1 = perguntas[0].get('Opções')

# print(pergunta1)
# print(opcoes1)
# resposta = str(input('Digite sua resposta: '))

# if resposta == perguntas[0].get("Resposta"):
#     print("Acertou")