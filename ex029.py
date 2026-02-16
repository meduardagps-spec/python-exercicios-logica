v=float(input('Qual a sua velocidade em km/h?'))
if v>80:
    t=v-80
    print("Você está acima da velocidade permitida!")
    print("Deve uma multa de {:.2f} reais!".format(t*7))

else:
    print("Tenha um bom dia! Dirija com segurança!")