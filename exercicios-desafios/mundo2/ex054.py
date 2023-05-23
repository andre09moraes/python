import datetime
totmaior = 0
totmenor = 0
ano = datetime.date.today().year
for c in range(1, 8):
    nasc = int(input('Que ano a {}ª nasceu? '.format(c)))
    idade = ano - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} pessoas de maior, e {} pessoas menor de idade'.format(totmaior, totmenor))
