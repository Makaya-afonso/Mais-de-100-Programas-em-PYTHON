# escreva um programa que faça o computador "pensar" em um numero
# inteiro entre 0 à 5 e faça peça para usuario tentar descobrir
# qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
import time
lista = [0,1,2,3,4,5]
computador = random.choice(lista)
usuario = int(input('Qual foi o número escolhido pelo computador?: '))
time.sleep(2)
if usuario == computador:
    print('Para bem você venceu')
else:
    print('Você perdeu, tenta novamente')
print('O número escolhido pelo computador é {}'.format(computador))