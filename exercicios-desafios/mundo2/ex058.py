import random
import time
print('Tente adivinhar o número que o PC pensou')
num = random.randint(0, 10)
jogador = int(input('Digite um número de 0 a 10: '))
tent = 0
while jogador != num:
    time.sleep(1)
    print('Processando...')
    tent += 1
    jogador = int(input('Número errado, digite novamente: '))
    if jogador < num:
        print('O número é maior')
    elif jogador > num:
        print('O número é menor')
print('Você acertou em {} tentativas, o número era {}'.format(tent, jogador))

'''
Correção

computador = randint(0, 10)
acertou = false
palpites = 0
while not acertou:
    jogador = int(input('Digite novamente: '))
    palpites += 1
    if jogador == computador
        acertou = true
    else:
        if jogador < computador:
            print('Maior')
        elif jogador > computador:
            print('Menor')
print('Acertou com {} tentativas'.format(palpites))
'''