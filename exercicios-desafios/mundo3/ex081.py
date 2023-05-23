numeros = list()

while True:
    numeros.append(int(input('Digite um valor: ')))
    res = str(input('Deseja continuar? [S/N] ')).lower().strip()
    if res == 'n':
        break
print('-' * 30)
print(f'Foram digitados {len(numeros)} valores.')
numeros.sort(reverse=True)
print(f'A lista ordenada em ordem decrescente é {numeros}.')
if 5 in numeros:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado.')
print('-' * 30)
