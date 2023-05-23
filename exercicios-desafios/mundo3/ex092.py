import datetime
info = dict()
ano = datetime.date.today().year
info['nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
info['idade'] = ano - idade
info['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
while True:
    if info['CTPS'] == 0:
        break
    else:
        info['ano de contratacao'] = int(input('Ano de contratação: '))
        info['salario'] = float(input('Salário: R$'))
        info['aposentadoria'] = (info['ano de contratacao'] + 35) - idade
        break
print('-=' * 30)
for k, v in info.items():
    print(f'  - {k} tem o valor {v}')
