cadastro = list()
princ = list()
maior = menor = 0
while True:
    cadastro.append(str(input('Nome: ')))
    cadastro.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        elif cadastro[1] < menor:
            menor = cadastro[1]
    princ.append(cadastro[:])
    cadastro.clear()

    cont = str(input('Deseja continuar? [S/N] ')).lower()
    if cont == 'n':
        break
print('-*' * 20)
print(f'O total de pessoas cadastradas foram {len(princ)}.')
print(f'O maior peso foi de {maior:.2f} Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
        print()
print(f'O menor peso foi de {menor:.2f} Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
