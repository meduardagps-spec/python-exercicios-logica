import time
print( "Vou escolher um número inteiro de 0 a 5... Tente advinhar!")

time.sleep(2)
print("PROCESSANDO...")

time.sleep(3)
import random
nc=random.randint(0, 5)
nu=int(input("Tente acertar o número inteiro escolhido por mim:"))

if nc==nu:
    print("Parabéns! Você acertou!")

else:

    print("Que pena, eu pensei no {}! Você errou!".format(nc))
