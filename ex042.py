# Refaça o Desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos lados são iguais
# Isóceles: dois lados iguais
# Escaleno: todos lados são diferents

r1 = float(input('A medida da primeira reta: '))
r2 = float(input('A medida da segunda reta: '))
r3 = float(input('A medida da terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas acima podem formar um triângulo.')
    if r1 == r2 == r3:
        print('E formam um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('E formam um triângulo ISÓSCELES.')
    else:
        print('E formam um triângulo ESCALENO.')
else:
    print('As retas acima não podem formar um triângulo.')