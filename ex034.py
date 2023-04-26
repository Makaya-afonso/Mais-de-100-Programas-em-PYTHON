# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R1250, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Quanto você ganha?: '))
aumento1 = salario + 10/100*salario
aumento2 = salario + 15/100*salario
if salario > 1500:
    print('Você terá um aumento de 10%, passando de {} para {}'.format(salario,aumento1))
else:
    print('Você terá um aumento de 15%, passando de {} para {}'.format(salario,aumento2))