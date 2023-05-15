produtos = ('lapis', 1.50, 'caderno', 10, 'mouse', 30, 'teclado mecânico', 100, 'monitor', 1000, 'navio de brinquedo', 30)
print('-' * 39)
print('{:^39}'.format('Lista de preços'))
print('-' * 39)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 39)
