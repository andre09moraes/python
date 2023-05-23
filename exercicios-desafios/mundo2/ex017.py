import math

catetoOposto = float(input('Digite o valor do cateto oposto: '))
catetoAdjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.sqrt(catetoOposto ** 2 + catetoAdjacente ** 2)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))

'''Também tem como fazer da seguinte forma:
math.hypot(catetoOposto, cateto Adjacente)'''