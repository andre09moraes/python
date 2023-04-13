sexo = str(input('Qual é o seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Valor incorreto, digite novamente: ')).strip().upper()[0]
print('Entendi, seu sexo é {}'.format(sexo))
