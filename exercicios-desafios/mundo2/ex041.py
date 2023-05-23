import datetime

nasc = int(input('Digite seu ano de nascimento: '))
idade = datetime.date.today().year - nasc
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('Você é da categoria Mirim.')
elif idade <= 14:
    print('Você é da categoria Infantil')
elif idade <= 19:
    print('Você é da categoria Junior')
elif idade <= 20:
    print('Você é da categoria Sênior')
else:
    print('Você é da categoria Master')
