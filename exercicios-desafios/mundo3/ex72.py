cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número: '))
    if 0 <= num <= 20:
        break
    else:
        print('Número invalido, digite um número entre 0 e 20.')
print(f'Você digitou {cont[num]}')
