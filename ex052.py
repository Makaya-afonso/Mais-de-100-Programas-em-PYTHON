# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
contagem = 0
num = int(input('Digite um número: '))
for cont in range(1, num+1):
    if num % cont == 0:
        print('\033[34m', end=' ')
        contagem += 1
    else:
        print('\033[31m',  end=' ')
    print('{}'.format(cont), end=' ')
print('\n\033[mO número {} foi divido {} vezes'.format(num, contagem))
if contagem == 2:
    print('Por isso, {} é PRIMO!'.format(num))
else:
    print('Por isso, {} NÂO É PRIMO!'.format(num))