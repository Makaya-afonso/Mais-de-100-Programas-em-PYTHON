# Escreva um programa que converte uma temperatura
# digitada em °C e converte para °F.

c = float(input('Digite a temperatura em °C: '))
f = 1.8*c + 32

print('{}°C corresponde à {}°F'.format(c,f))