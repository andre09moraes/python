import time

print('-' * 15)
print('Analisador de triângulos')
print('-' * 15)
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
print('\033[31mAnalisando às retas...\033[m')
time.sleep(2)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mOs segmentos acima podem formar um triângulo\033[m')
else:
    print('\033[7;30;41mOs segmentos não podem formar um triângulo\033[m')
