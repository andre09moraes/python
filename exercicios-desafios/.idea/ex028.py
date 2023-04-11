import random
num = random.randint(0, 5)
tent = int(input('Digite um número de 0 a 5: '))
if tent == num:
    print('Parabéns, você acertou!')
else:
    print('Você errou, o número era {}'.format(num))
