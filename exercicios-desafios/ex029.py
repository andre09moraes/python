vel = float(input('Qual velocidade você estava (Km): '))
multa = (vel - 80) * 7
if vel > 80:
    print('Você está acima da velocidade, foi multado!')
    print('Sua multa será de {:.2f}'.format(multa))
else:
    print('Você esta na velocidade correta, continue assim.')
