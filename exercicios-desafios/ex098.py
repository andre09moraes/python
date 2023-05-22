from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    sleep(1)
    print('-' * 50)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(.2)
            cont += p
        print('FIM')
        print('-' * 50)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(.1)
            cont -= p
        print('FIM')
        print('-' * 50)


contador(0, 100, 10)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem.')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
