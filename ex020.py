a=str(input('Aluno 1:'))
b=str(input('Aluno 2:'))
c=str(input('Aluno 3:'))
d=str(input('Aluno 4:'))
from random import shuffle
lista=[a,b,c,d]
shuffle(lista)
print("A ordem dos alunos sorteados é {} ".format(lista))