#Quando estamos trabalhando com string as vezes queremos
#usar apenas algumas partes e usand o list comprehensin fia
#muito fácil essa necessidade
string ='1234567890123456789034237842347'

print (string[0:10])
print (string[10:20])
print (string[20:30])

n = 10
comp2 = [(i,i + n)for i in range(0,len(string), n)]

print (comp2)

comp3 = [string[i:i +n]for i in range(0,len(string),n)]
print (comp2)