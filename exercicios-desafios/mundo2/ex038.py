n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 < n2:
    print('O {} é o maior'.format(n2))
elif n1 == n2:
    print('Os números tem o mesmo valor.')
else:
    print('O {} é o maior'.format(n1))
