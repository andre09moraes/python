from time import sleep

def maior(* num):
    cont = maior = 0
    print('\nAnalizando os valores')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    sleep(.5)
    print(f'O maior valor informado foi {maior}.')
    sleep(.5)
    print('-' * 50)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
