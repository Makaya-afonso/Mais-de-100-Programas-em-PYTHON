# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# até 9anos: MIRIM
# até 14anos: INFANTIL
# até 19anos: JÚNIOR
# até 20anos: SÊNIOR
# acima: MASTER
from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano

if idade <= 9:
    print('O atleta tem {} anos e está na categoria MIRIM'.format(idade))
elif idade >= 10 and idade <= 14:
    print('O atleta tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade >= 15 and idade <= 19:
    print('O atleta tem {} anos e está na categoria JÚNIOR'.format(idade))
elif idade >= 20 and idade <= 20:
    print('O atleta tem {} anos e está na categoria SÊNIOR'.format(idade))
else:
    print('O atleta te {} anos e está na categoria MASTER'.format(idade))