valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
print('-=' * 20)
print(f'Os números digitados foram {valores}.')
print(f'O maior número digitado foi {max(valores)}, na posição {valores.index(max(valores))}')
print(f'O menor número digitado foi {min(valores)}, na posição {valores.index(min(valores))}')

'''
listanum = []
mai = 0
men = 0
for c in range (0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai}, nas posições ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men}, nas posições ', end='')
for i, v enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
'''