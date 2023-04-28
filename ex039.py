# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar. Se é a hora de se alistar.
# Se já passou o tempo do alistamento.
# O seu programa também  deverá mostar o tempo que falta ou que ja passou o prazo.

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento,idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam  {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('O seu alistamento será em {}'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('O seu alistamento foi em {}'.format(ano))

