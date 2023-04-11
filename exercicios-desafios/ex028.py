import random
from time import sleep #Ele acrescenta isto na resolução do exercicio

num = random.randint(0, 5)
print('Adivinhe que número estou pensando de 0 a 5.')
adv = int(input('Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3) #Ele acrescentou na resolução do exercicio.
if adv == num:
    print('Parabéns você acertou!')
else:
    print('Você é ruim em! O número era {}.'.format(num))
