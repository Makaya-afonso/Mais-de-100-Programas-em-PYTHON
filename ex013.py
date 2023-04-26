# Faça um algoritmo que leia o salário de um fucionário
# e mostre seu novo salário , com 15% de aumento.

salario = float(input('Digite o valor salarial: '))

novosalario = salario + (15/100)*salario

print('O foncionário que ganhava {}, passou a ganha {:.2f}'.format(salario,novosalario))