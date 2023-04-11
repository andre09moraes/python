import datetime #adicionou na correção do exercicio

ano = int(input('Em que ano você está? Coloque 0 para analisar o ano atual: '))
if ano == 0: #adicionou na correção do exercicio
    ano = datetime.date.today().year #adicionou na correção do exercicio
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
