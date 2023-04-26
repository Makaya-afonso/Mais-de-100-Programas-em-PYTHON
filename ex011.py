# Faça um programa que leia a largura e a altura de
# uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária pintá-lo , sabendo cada litro de
# tinta, pinta uma área de 2m²   1l = 2m²

largura = float(input('Digite a largura em metros: '))
altura = float(input('Digte a altura em metros: '))

area = largura*altura
litros = (1*area)/2

print('A sua parede tem {:.2f}m² de área, e a quantidade necessária de tinta é de {:.2f}L'.format(area,litros))