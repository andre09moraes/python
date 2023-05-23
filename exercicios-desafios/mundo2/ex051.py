termo = int(input('Digite um valor: '))
razao = int(input('Digite outro valor: '))
for c in range(termo, 11, razao):
    print(c)

'''
Correção

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range('primeiro, decimo, razao):
    print('{} '.format(c), end=' ')
print('Acabou.')

'''