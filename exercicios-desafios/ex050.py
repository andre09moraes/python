s = 0
for c in range(1, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
    else:
        print('\033[1;31mO número não é impar\033[m')
print(s)
