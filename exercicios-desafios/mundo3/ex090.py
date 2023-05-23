boletim = {}

boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input(f'Média do {boletim["Nome"]}: '))
print('-=' * 30)

for p, n in boletim.items():
    print(f'- {p} é {n}')

if boletim['Média'] <= 5:
    boletim['situacao'] = 'Reprovado'
    print(f'- A situação é {boletim["situacao"]}.')
elif boletim['Média'] <= 7:
    boletim['situacao'] = 'Recuperação'
    print(f'- A situação é {boletim["situacao"]}.')
else:
    boletim['situacao'] = 'Aprovado!'
    print(f'- A situação é {boletim["situacao"]}')
