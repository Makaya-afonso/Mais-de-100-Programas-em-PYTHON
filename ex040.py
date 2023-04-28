# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média:
# média abaixo de 5.0: reprovado
# média entre 5.0 a 6.9: recuperação
# média 7.0 ou superior: aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 =  float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5.0:
    print('A sua média é {} e você está Reprovado'.format(media))
elif media >= 5.0 and media < 7:
    print('A sua média é {} e você está em Recuperação'.format(media))
else:
    print('A sua média é {} e você está Aprovado'.format(media))