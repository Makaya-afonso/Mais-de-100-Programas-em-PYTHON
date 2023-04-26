# Crie um algoritmo que leia um número e
# mostre o seu dobro, tiplo e raiz quadrada
import math
num = int(input('Digite um número: '))
d = num*2
t = num*3
r = math.sqrt(num)

print('O dobro de {} é {}, \nseu triplo é {} e \nsua raiz quadrada é {:.2f}'.format(num,d,t,r))