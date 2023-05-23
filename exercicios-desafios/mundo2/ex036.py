casa = float(input('Qual é o valor da casa: R$'))
salario = float(input('Qual é o seu sálario: R$'))
parcelas = int(input('Quantos anos você vai pagar: '))
parcelasMeses = parcelas * 12
valorParcelas = casa / parcelasMeses
if valorParcelas > salario * 0.30:
    print('Infelizmente a compra não será possivel, serão {} parcelas de R${:.2f}.'.format(parcelasMeses, valorParcelas))
else:
    print('Parabéns! O emprestimo foi aprovado, serão {} parcelas de R${:.2f}'.format(parcelasMeses, valorParcelas))
