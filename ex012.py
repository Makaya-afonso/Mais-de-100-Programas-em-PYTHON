# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto: '))

novopreço = preço - 5/100*preço

print('O produto que custava {}, agora com 5% de desconta, ta custando {:.2f}'.format(preço,novopreço))