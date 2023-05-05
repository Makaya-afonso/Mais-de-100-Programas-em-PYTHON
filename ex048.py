# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três que se encontram no intervalo de 1 até 500.
print('Os números ímpares múltiplos de três são:')
s = 0
contar = 0
for cont in range(1,501,2):
    if cont % 3 == 0:
        s += cont
        contar += 1
        print(cont, end=' ')
print('\n   São {} números no total. E a somas desses números é {}'.format(contar,s))

