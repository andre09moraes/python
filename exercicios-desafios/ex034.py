sal = float(input('Digite seu salário: R$'))
salAcima = sal + (sal * 0.10)
salAbaixo = sal + (sal * 0.15)
if sal <= 1250:
    print('Seu salário com um aumento de 15% será de {:.2f}.'.format(salAbaixo))
else:
    print('Seu salário com um aumento de 10% será de {:.2f}'.format(salAcima))

'''
CORREÇÃO GUANABARA
salario = float(input('Qual é o seu salário: R$'))
if salario <= 1250:
    novo = salario + (sal * 0.15)
else:
    novo = salario + (sal * 0.10)
print('Quem ganhava R${} passa a ganhar R${} agora.'.format(salario, novo))
'''