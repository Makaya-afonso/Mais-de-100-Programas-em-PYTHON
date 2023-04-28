# Densevolva uma lógica que leia o peso e altura de uma pessoa,
# calcule o seu IMC e mostra seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 a 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade  Acima de 40: Obesidade mórbida

peso = float(input('Digite o peso em kg: '))
altura = float(input('Digite a altura: '))

imc = peso/(altura**2)
print('O seu IMC é de {:.2f}m'.format(imc))

if imc < 18.5:
    print('Você está a baixo do peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está em sobrepeso.')
elif 30 <= imc < 40:
    print('Você está em obesidade.')
elif imc >= 40:
    print('Você está em obesidade móbida, cuidado!')
