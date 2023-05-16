valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado.')
    else:
        print('Valor duplicado!')
    r = str(input('Quer continuar? [S/N] ')).lower().strip()
    if r in 'n':
        break
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
