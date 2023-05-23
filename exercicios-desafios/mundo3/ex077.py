palavras = ('caderno', 'mouse', 'curso', 'python', 'trabalhar',
            'programador', 'futuro', 'aprender', 'praticar', 'ilustrador', 'manga')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
