# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro nome e o ultimo nome separadamente

nome = input('Digite o seu nome: ')
dividido = nome.split()
print('O primeiro nome é', dividido[0])
print('O segundo nome é', dividido[-1])