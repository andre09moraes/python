import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(an, cos))
print('O ângulo de {} tem a tangente de {:.2f}'.format(an, tan))


'''
O QUE EU FIZ

import math
angulo = float(input('Digite o ângulo: '))
print('O coseno do ângulo {}º é {:.2f} e o seno é {:.2f}'.format(angulo, math.cos(angulo), math.sin(angulo)))
'''