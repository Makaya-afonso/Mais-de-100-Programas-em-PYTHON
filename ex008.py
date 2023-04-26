# Escreva um programa que leia um valor em metros
# e o exiba convertido em centimetros e milimetros.

valor = float(input('Digite um valor em Metros: '))

centi = valor*100
deci = valor*10
print('{}m vale {}cm e \n{}dm'.format(valor,centi,deci))