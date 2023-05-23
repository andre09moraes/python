numeros = list()
par = list()
impar = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    res = str(input('Quer continuar? [S/N] ')).lower().strip()
    if 'n' in res:
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 30)
print(f'A lista digitada foi {numeros}.')
print(f'Os números pares digitados foram {par}.')
print(f'Os números impares digitados foram {impar}.')
