import random
n1 = input('Digite um nome: ')
n2 = input('Digite outro nome: ')
n3 = input('Digite outro nome: ')
n4 = input('Digite mais um nome: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))


'''
O QUE EU FIZ

import random
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
num = random.randint(1, 4)
print('O aluno {} foi escolhido.'.format(num))
'''