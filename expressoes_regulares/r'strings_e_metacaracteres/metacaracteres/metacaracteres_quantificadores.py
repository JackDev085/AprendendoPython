#para contonar o uso de palavras com vícios de lingugagens podemos
#usar os metacaracteres quantificadores
import re
frase = 'Nãããããããoooooo esquecer de ir para a academia, não deixar para depois'


print(re.findall(r'não',frase, flags=re.I))
#O resultado esperado depois dessa funcao "findall()" para essa
#frase seria duas palavras 'não'. Devido ao uso indiferente da linguagem
#Para esse palavra em questão (nã0) o interpretador não conseguiu achar mais de
#uma reincidência

"""Metacarcteres

. = procura por reincidências de palavras e o ponto seria onde seria o conteúdo de busca
[] = pode ser utilizado para adicionar elementos na procura
* = significa que determinado elemento da string pode repetir o ou um número ilimitado de vezes
+ = significa que um certo elemento se repetirá 1 ou ilimitadas vezes
? = significa que um determinado elemento se repetirá 0 ou 1 vez na string
{} = significa que um elemento especifíco da string se repetirá dentro de um intervalo definido
"""

mensagem = 'Nãããããããoooooo esquecer de ir para a academia, não deixar para depois'
print(re.findall(r'não',mensagem, flags=re.I)) #[não]

print(re.findall(r'Nã+o',mensagem)) #[Nããããããão]
print(re.findall(r'Nã+o+',mensagem)) #[Nãããããããoooooo]
print(re.findall(r'[Nn]ã+o+',mensagem)) #[Nãããããããoooooo', não]
print(re.findall(r'nã+o+',mensagem, flags=re.I)) #[nããããããããããooo, não]

#Podemos utilizar esses metacaracteres de muitas formas, mas sempre prezando
#pela legibildiade do código e usar quando necessário
nome = 'Fernnnnnnannnnnnndo'
print(re.findall(r'fern+an+do',nome,flags=re.I))
