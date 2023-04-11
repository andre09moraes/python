import datetime

nascimento = int(input('Digite seu ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nascimento
if idade == 18:
    print('Você está na idade de se alistar.')
elif idade < 18:
    print('Você não está na idade de se alistar ainda, faltam {} anos para se alistar'.format(18 - idade))
else:
    print('Você passou da idade de se alistar, passou {} anos'.format(idade - 18))
