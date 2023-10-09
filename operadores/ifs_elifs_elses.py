#if = se
a = 34
b = 33
c = 35

if a > b:
    print('A é maior que B')
#elif = mas se
#============================================================
if a < b: # quando o if é dado como falso ele parte para o próximo bloco de código
    print('A é maior que B')
elif c > a: # caso também seja falso ele irá para o próximo bloco de código
    print('C é maior que A')
#else se não
#============================================================
if a < b:
    print('A é maior que B')
elif c < b: 
    print('C é menor que B')
else: #caso nenhuma das condições seja verdadeira, entrará no bloco do else
      #e realizará o bloco de código
    print('B é menor que C')


    # operador AND = significa 'e'
if a > b and b < c: #Testa duas condições na estrutura if caso as duas condições sejam verdadeiros executará o trecho de código
    print('A é maior que B e B é menor que C')
   

    # operador OR = sigfica 'ou'

if a < b or b < c: #Testa duas condições na estrutura if caso uma das condições sejam verdadeiros executará o trecho de código
    print('A é maior que B e B é menor que C')