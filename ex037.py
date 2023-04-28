# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base da conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

num = int(input('Digite um número inteiro: '))
print('Qual a base da converão? \nPrima 1 para binário \nPrima 2 para octal \nPrima 3 para hexadecimal')
base = int(input('Qual será a base?: '))
if base == 1:
    print('{} convertido para BINÁRIO é {}'.format(num,bin(num)))
elif base == 2:
    print('{} convertido para OCTAL é {}'.format(num,oct(num)))
elif base == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num,hex(num)))
else:
    print('Opção Inválida,tente 1 , 2 ou 3')