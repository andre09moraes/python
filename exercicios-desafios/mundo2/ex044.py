preco = float(input('Preço das compras: R$'))
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 0.10)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 2:
    total = preco - (preco * 0.05)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros.'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 0.20)
    totalParcelas = int(input('Quantas Parcelas? '))
    parcela = total / totalParcelas
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(totalParcelas, parcela))
else:
    print('Opção invalida, tente novamente.')
