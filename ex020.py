# O mesmo professor do desafio anterior quer sortear
# a ordem de apresentação dos alunos. Faça um programa
# que leia o nome dos alunos quatro alunos e mostre na a ordem sorteado

import random
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
print(lista)