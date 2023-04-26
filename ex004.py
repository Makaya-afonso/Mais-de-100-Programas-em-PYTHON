# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo trimitivo, e todas informações possiveis sobre ele

algo = input('Digite Algo: ')
print('Tipo Primitivo:', type(algo))
print('É alfanumérico?', algo.isalnum())
print('É alfa?', algo.isalpha())
print('É menúscula?', algo.islower())
print('É numérico?', algo.isnumeric())
print('É maiúsculo?', algo.isupper())