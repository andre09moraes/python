nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}.'.format(dividido[0]))
print('Seu ultimo nome é {}.'.format(dividido[len(dividido)-1]))


'''
nome = input('Digite seu nome e sobrenome: ')
dividido = nome.split()
print(dividido[0])
print(dividido[1])
'''