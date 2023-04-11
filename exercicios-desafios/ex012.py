preco = float(input('Qual é o preço? R$'))
desconto = preco - (preco * 0.05)
print('O produto é R${:.2f} com 5%OFF fica R${:.2f}'.format(preco, desconto))
