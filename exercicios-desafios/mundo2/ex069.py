maior18 = 0
homem = 0
mulher20 = 0
while True:
    print('-' * 20)
    print('Cadastre uma pessoa')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Cadastro encerrado.')
print(f'Temos {maior18} maiores de 18 anos, {homem} homens e {mulher20} mulher com menos de 20 anos.')
