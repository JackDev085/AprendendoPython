#Com o método re.find(all) podemos atestar todos as
#reincidências de uma certa palavra em uma variável de texto
#ou frase.

#Pois bem agora com o método re.sub() podemos reescrever alguma palavra no lugar de outra
#ex abaixo

import re
texto1 = ('No dia trinta de março de dois mil e vinte foi inaugurado'
          'o novo ginásio de esportes da escola estadual Professor Annes Dias, na cidade de '
          'Cruz Alta, no estado do Rio Grande do Sul. A obra inciialmente '
          'crçada em um milhão de reai acabou não utilizando de todo o recurso,'
          'uma vez que dois grandes empresários da cidade, João Fagundes e Maria Terres doaram juntos'
          'em torno de duzentos mil reais. João Fagundes se manifestou dizendo que apoiou a obra pois acredita no desenvolvimento'
          'da cidade, assim investe regularmente para hospitais'
          'e escolas da mesma . Maria Terres não quis se pronunciar'
          'sobre o asunto.')
#método re.sub(string , stringSubstituta ,varDeTexto) flags = re.I (usado para tornar todas as variáveis em minusculuas)
print(re.sub('João' , 'Carlos', texto1, flags=re.I)) #No dia trinta de março de dois mil e vinte foi inauguradoo novo ginásio de esportes da escola estadual Professor Annes Dias, na cidade de Cruz Alta, no estado do Rio Grande do Sul. A obra inciialmente crçada em um milhão de reai acabou não utilizando de todo o recurso,uma vez que dois grandes empresários da cidade, Carlos Fagundes e Maria Terres doaram juntosem torno de duzentos mil reais. Carlos Fagundes se manifestou dizendo que apoiou a obra pois acredita no desenvolvimentoda cidade, assim investe regularmente para hospitaise escolas da mesma . Maria Terres não quis se pronunciarsobre o asunto.


#Já a função match('palavra , varDeTexto) é usado para verificar se a primeira palavra do texto condiz com a palavra verifiada
#do método
texto2 = 'fernando chegará essa noite'
print(re.match(r'fernando' , texto2)) #<re.Match object; span=(0, 8), match='fernando'>
print(re.match(r'noite' , texto2)) #None

#A função re.split('separador (ex: ','), variavelDeTexto ')
texto3 = "que dia bonito, vou tomar café"


print(re.split(',',texto3)) #['que dia bonito', ' vou tomar café']