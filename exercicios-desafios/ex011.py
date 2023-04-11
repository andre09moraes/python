largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))
area = altura * largura
litro = 2
print('Você precisará de {:.0f}l de tinta para pintar {:.2f}m².'.format(area / litro, area))
