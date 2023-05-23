valor = float(input('Digite um valor: R$'))
dolares = 5
quantidade = valor / dolares
print('Você tem R${} e pode comprar U${:.2f} dolares.'.format(valor, quantidade))
