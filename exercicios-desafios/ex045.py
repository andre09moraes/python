from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Sua ações:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('O Computador escolher {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: #pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('\033[1;32mJogador vence\033[m')
    elif jogador == 2:
        print('\033[1;31mComputador vence\033[m')
    else:
        print('Jogada inválida.')
elif computador == 1: #papel
    if jogador == 0:
        print('\033[1;31mComputador vence\033[m')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('\033[1;32mJogador vence\033[m')
    else:
        print('Jogada inválida.')
elif computador == 2: #tesoura
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('\033[1;31mComputador vence\033[m')
    elif jogador == 2:
        print('Empate')
    else:
        print('\033[1;32mJogada inválida.\033[m')
