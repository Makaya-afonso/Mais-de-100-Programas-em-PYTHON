# Faça um programa que leia três números
# e mostre qual é maior e qual é o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1 > num2 and num3:
    print('O número maior é {}'.format(num1))
elif num2 > num3 and num1:
    print('O número maior é {}'.format(num2))
else:
    print('O número maior é {}'.format(num3))

if num2 > num1 < num3:
    print('O número menor é {}'.format(num1))
elif num3 > num2 < num1:
    print('O número menor é {}'.format(num2))
elif num1 > num3 < num2 :
    print('O número menor é {}'.format(num3))