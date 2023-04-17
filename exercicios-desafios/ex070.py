total = 0
produto1000 = 0
menor = 0
cont = 0
barato = ''
while True:
    print('-' * 30)
    print('{:-^30}'.format('Loja super baratão'))
    print('-' * 30)
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco >= 1000:
        produto1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^30}'.format('Compra finalizada.'))
print(f'O total de gasto na compra foi de R${total:.2f}')
print(f'Temos {produto1000} produtos acima de R$1000,00')
print(f'O produto mais barato foi o {barato} de R${menor:.2f}')
