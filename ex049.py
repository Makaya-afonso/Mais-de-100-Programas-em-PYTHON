# Refaça o desafio 009, mostrando a tabuada de multiplicação de um
# número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('digite um número: '))
print('=' * 14)
for cont in range(1,13):
    print('{} * {} = {}'.format(n,cont,cont*n) )
print('=' * 14)