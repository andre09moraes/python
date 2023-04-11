num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num  // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))


'''
num = input('Digite um número: ')
num0 = num[0]
num1 = num[1]
num2 = num[2]
num3 = num[3]
print('Unidade {}, dezena {}, centena {} e milhar {}.'.format(num3, num2, num1, num0))
'''