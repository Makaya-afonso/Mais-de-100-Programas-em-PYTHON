# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o
s = 0
contagem = 0
for cont in range(1,7):
    num = int(input('Digite o {} número inteiro: '.format(cont)))
    if num % 2 == 0:
        s += num
        contagem += 1
print('São {} números pares no total.'.format(contagem))
print('O somatório de todos números pares é {}.'.format(s))