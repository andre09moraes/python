from time import sleep

num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair
    ''')
    opcao = int(input('Qual é sua opção? '))
    if opcao == 1:
        soma = num1 + num2
        print('{} + {} = {}'.format(num1, num2, soma))
    elif opcao == 2:
        mult = num1 * num2
        print('{} x {} = {}'.format(num1, num2, mult))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('O maior número é {}'.format(maior))
    elif opcao == 4:
        print('Informe os números novamente.')
        num1 = int(input('Digite novamente: '))
        num2 = int(input('Digite novamente: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente.')
    print('-=' * 16)
    sleep(1)
print('Fim do programa.')
