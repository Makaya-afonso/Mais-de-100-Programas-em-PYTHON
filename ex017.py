# Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa
import math
a = float(input('Digite o valor do cateto oposto: '))
b = float(input('Digite o valor do cateto adjacente: '))

c = math.sqrt(a**2 + b**2)
print('O comprimento da hipotenusa é de {}m²'.format(c))