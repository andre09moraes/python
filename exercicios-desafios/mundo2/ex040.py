mate = float(input('Digite sua nota de matemática: '))
port = float(input('Digite sua nota de Português: '))
media = (mate + port) / 2
if media <= 5:
    print('Sua média foi {}, você foi reprovado.'.format(media))
elif media <= 6.9:
    print('Sua média foi {}, você está de recuperação.'.format(media))
elif media <= 10:
    print('Sua média foi {}, você foi aprovado!'.format(media))
