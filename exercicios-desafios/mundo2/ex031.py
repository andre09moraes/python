dis = float(input('Qual é a distância (Km): '))
valorAbaixo = dis * 0.50
valorAcima  = dis * 0.45
if dis <= 200:
    print('O valor da passagem será de R${:.2f}.'.format(valorAbaixo))
else:
    print('O valor da passagem será de R${:.2f}.'.format(valorAcima))
