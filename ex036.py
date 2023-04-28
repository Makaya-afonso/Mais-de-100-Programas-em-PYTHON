# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
# o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# calcular o valor da prestação mensal,
# sabendo que ele não pode exceder 30% do salário ou então o empréstimo será negado.

valordacasa = float(input('Qual é o valor da casa?: '))
salario = float(input('Quanto é o seu salário?: '))
anos = int(input('Em quantos anos você vai pagar?: '))

prestação = valordacasa/(anos*12)
TrintaPorcentoDoSalario = 30/100 * salario

print('Para pagar uma casa de R${}, em {}anos a pretação será de R${:.2f} mensal'.format(valordacasa,anos,prestação))
if prestação > TrintaPorcentoDoSalario:
    print('Empréstimo NEGADO!')
    print('Prestação Excede 30% do seu Salário')
else:
    print('Empréstimo pode ser CONCEDIDO')