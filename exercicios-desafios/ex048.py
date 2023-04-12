s = 0
n = 1
for c in range(1, 501):
    if c % 2 == 1:
        print(c)
        s += n
print('A soma dos valores é {}'.format(s))

'''
Correção

soma = 0
cont = 0
for c in range(1, 501):
    if c % 3 == 0:
        cont =+ 1
        soma =+ c
print(soma, cont)

'''