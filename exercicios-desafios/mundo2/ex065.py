res = 'S'
soma = quant = media = maior = menor = 0
while res in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    res = str(input('Quer continuar? [s/n] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
