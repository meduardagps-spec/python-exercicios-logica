aluno_1 = str(input('Aluno 1:'))
aluno_2 = str(input('Aluno 2:'))
aluno_3 = str(input('Aluno 3:'))

lista = [ aluno_1 , aluno_2 , aluno_3 ]

from random import shuffle
shuffle(lista)

print(f"A ordem dos alunos sorteados é {lista}.")
