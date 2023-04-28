# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão : 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou  mais no cartão: 20% de juros

preço = float(input('PREÇO DAS COMPRAS?: R$ '))
print('''== COMO VOCÊ DESEJA PAGAR? ==
PRIMA [1] PARA PAGAMENTO À VISTA, DINHEIRO/CHEQUE
PRIMA [2] PARA PAGAMENTO À VISTA NO CARTÃO
PRIMA [3] PARA PAGAMENTO ATÉ 2X NO CARTÃO
PRIMA [4] PARA PAGAMENTO ATÉ 3X OU MAIS NO CARTÃO''')
metodo = int(input('Método de pagamento: '))

if metodo == 1:
    novo = preço - 10/100 * preço
    print('VOCÊ TERÁ UM DESCONTO DE 10%. PAGANDO APENAS R${:.2f}.'.format(novo))
elif metodo == 2:
    novo = preço - 5/100 * preço
    print('VOCÊ TERÁ UM DESCONTO DE 5%. PAGANDO APENAS R${:.2f}.'.format(novo))
elif metodo == 3:
    parcela = preço/2
    print('VOCÊ VAI PAGAR R${:.2f} 2X NO CARTÃO.'.format(parcela))
elif metodo == 4:
    parcelas = int(input('QUANTAS PARCELAS?: '))
    juros = preço + 20/100 * preço
    parcela = juros / parcelas
    print('VOCÊ VAI PAGAR R${:.2f} {}X NO CARTÃO. TOTAL R${:.2f} com 20% de juros.'.format(parcela,parcelas,juros))
else:
    print('MÉTODO INVÁTIDO, TENTE [1] , [2] , [3] OU [4]')
