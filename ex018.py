# Faça um programa que leia um ângulo qualquer e mostre
# na tela o valor do seno, cosseno e tangete desse ângulo.

import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(angulo)
cos = math.cos(angulo)
tang = math.tan(angulo)
print('O ceno de {} é {}'.format(angulo,seno))
print('O cosseno de {} é {}'.format(angulo,cos))
print('A tangente de {} é {}'.format(angulo,tang))