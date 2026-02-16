from random import choice
aluno_1 = str(input('Nome do primeiro aluno:'))
aluno_2 = str(input('Nome do segundo aluno:'))
aluno_3 = str(input('Nome do terceiro aluno:'))
aLundo_4 = str(input('Nome do quarto aluno:'))
Lista = [ aluno_1 , aluno_2 , aluno_3 , aluno_4 ]
escolhido = choice(Lista)
print(f'A pessoa sorteada é {escolhido}!')



