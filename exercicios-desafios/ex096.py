def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é {a} metros quadrados.')


print('Controle de Terrenos')
print('-' * 30)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
