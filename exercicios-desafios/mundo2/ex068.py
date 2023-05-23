from random import randint

print('-' * 20)
print('Jogo do par ou impar')
print('-' * 20)

v = 0
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você quer par ou impar [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}, o total foi de {total}. ', end='')
    print('Deu par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu.')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu.')
            v += 1
        else:
            print('Você perdeu.')
            break
print(f'Game over! Você venceu {v}x')