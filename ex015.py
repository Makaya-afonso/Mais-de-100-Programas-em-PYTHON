# Escreva um programa que pergunta a quantidade de km percorrido
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custar R60 por dia e R0.15 por km rodado.

dias = int(input('Digite a quantidade de dias alugado: '))
km = float(input('Digite a quantidade de km percorrido: '))
pago = dias*60 + km*0.15

print('Você vai pagar {:.2f}Reais pelos dias alugado'.format(pago))
