# Faça um programa que leia um número inteiro e
# mostre na tela o seu sucessor e seu antecessor.

num = int(input('Digite um número inteiro: '))
s = num + 1
a = num - 1
print('O sucessor de {} é {}, e o seu antecessor é {}'.format(num,s,a))