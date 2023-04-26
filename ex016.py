# Crie um programa que leia um numero real
# e mostre na tela a sua porção inteira
import math
real = float(input('Digite um número real: '))
valorinteiro = math.trunc(real)
print('O número {} tem a parte inteira {}'.format(real,valorinteiro))
