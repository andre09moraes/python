n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.2f}'.format(m))
if m >= 6:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim em!')
print('Sempre estude!')
