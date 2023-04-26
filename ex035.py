# Desenvolva um programa que leia o compimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Valor da primeira reta: '))
r2 = float(input('Valor da segunda reta: '))
r3 = float(input('Valor da terceira reta: '))
if r1 < r2 + r3 and  r2 < r1 +r3 and r3 < r1 + r2:
    print('As retas acima formam um triângulo')
else:
    print('As retas acima não formam um triângulo')

