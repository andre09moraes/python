gols = list()
info = dict()
info['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {info["nome"]} jogou? '))
print('-=' * 25)
for c in range(0, total):
    gols.append(int(input(f'  Quantos gols na {c + 1}ª partida: ')))
info['gols'] = gols[:]
info['total'] = sum(gols)
print('-=' * 25)
print(info)
print('-=' * 25)
for k, v in info.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 25)
print(f'O jogador {info["nome"]} jogou {len(info["gols"])} partidas.')
for i, v in enumerate(info["gols"]):
    print(f'  => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {info["total"]} gols.')
