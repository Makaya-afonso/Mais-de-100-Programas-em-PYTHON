# Faça um programa que leia o nome de uma cidade
# e diga se ela começa ou não com o nome "SANTO"

nome = input('Digite o nome de uma cidade: ')
dividido = nome.split()
nome1 = dividido[0].upper()
print('SANTO' in nome1)