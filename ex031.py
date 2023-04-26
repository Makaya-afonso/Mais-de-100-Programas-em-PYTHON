# Denselvova um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R0,50 por Km para viagens de até 200km
# e R0,45 para viagens mais longas.

distancia = float(input('Qual o valor da distância da viagem: '))

valor1 = distancia*0.50
valor2 = distancia*0.45
if distancia <= 200:
    print('Você vai pagar R0,50 por Km')
    print('E o preço a pagar será de R{}'.format(valor1))
else:
    print('Você vai pagar R0,45 por Km')
    print('E o preço a pagar será de R{}'.format(valor2))