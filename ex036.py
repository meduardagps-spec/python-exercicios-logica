print('\033[7;37;40mOlá, Mundo!\033[m')
a=3
b=5
print('Os valores são \033[1;30;47m{}\033[m e \033[1;37;40m{}\033[m;.'.format(a,b))

cores = {'limpa' : '\033[m]' , 'azul' : '\033[34m' , 'vermelho' : '\033[31m', 'preto' : '\033[30m'}
print('O número sorteado foi {}{}{}'.format(cores['azul'] , a , cores['limpa']))