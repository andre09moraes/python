print('\033[4;34;43mOlá, mundo\033[m')
print('\033[7;31;40mAgora eu estou mudando mais coisas\033[m')
A = 3
B = 5
print('Os valores são \033[35;41m{}\033[m e \033[32;45m{}\033[m'.format(A, B))

nome = 'André'
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7;30m'}

print('Olha só que legal {}{}{}.'.format(cores['azul'], nome, cores['limpa']))
