# Escreva um programa que leia a velocidade de um carro.
# se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# a multa vai custa R7,00 por cada Km acima do limite

velocidade = float(input('Digite o valor da velocidade: '))
multa = (velocidade - 80)*7
if velocidade > 80:
    print('Você foi multado')
    print('Você tem R{} de multa a pagar'.format(multa))
else:
    print('Tenha bom dia! Dirija com segurança')