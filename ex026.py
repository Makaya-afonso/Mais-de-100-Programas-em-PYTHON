# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# em que posição ela aparece a primeira primeira vez
# em que posição ela aparecea última vez

frase = input('Digite uma frase: ').upper().strip()
print('A letra A aparece {} na frase'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A') + 1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A') + 1))
