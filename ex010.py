# crie um programa que leia quanto dinheiro uma pessoa
# tem na carteira e mostre quantos dolares ele pode
# comprar. considere 1uds = r3.27

dinheiro = float(input('Quanto você tem na conta?: '))

convert = dinheiro*1/3.27
print('Com {:.2f}R você pode comprar {:.2f}UDS'.format(dinheiro,convert))