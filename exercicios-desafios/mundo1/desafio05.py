import random

nome = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
lista = [nome, nome2, nome3]
random.shuffle(lista)
print('A ordem da lista é {}'.format(lista))
