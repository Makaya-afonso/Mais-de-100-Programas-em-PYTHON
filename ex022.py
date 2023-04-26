# Crie um programa que leia o nome completo de uma pessoa  e mostre:
# O nome com todas as letras em maúsculas
# O nome com todas minúsculas
# Quantas palavras ao seu todo(sem considerar espaços)
#  Quantas letras tem o primeiro nome

nome = input('Digite o seu nome: ').strip()
print('O seu nome em maiúsculas é {}'.format(nome.upper()))
print('O seu nome em minúscalas é {}'.format(nome.lower()))
print('O seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))