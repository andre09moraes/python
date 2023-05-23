print('=-' * 15)
print('Tabuada')
print('-=' * 15)
n = 0
while True:
    n = int(input('Digite um valor para calcular a tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        produto = n * c
        print(f'{n} x {c} = {produto}')
print('Acabou')
