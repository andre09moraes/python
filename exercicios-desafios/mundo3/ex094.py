pessoas = dict()
galera = list()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))

    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).lower()[0]
        if pessoas['sexo'] in 'mf':
            break
        else:
            print('ERRO! Responda apenas M ou F.')

    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).lower()[0]
        if resp in 'sn':
            break
        print('ERRO! Responda apenas S ou N.')

    if resp == 'n':
        break

media = soma / len(galera)
print('-=' * 25)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.0f} anos.')

print('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'f':
        print(f'{p["nome"]} ',end='')
print()

print('D) As pessoas acima da média são: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]}, ', end='')
print()

print('  << ENCERRADO >>  ')
