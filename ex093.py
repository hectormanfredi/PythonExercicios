# Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai ler o NOME DO JOGADOR e
# QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso será
# guardado em um dicionário, incluindo o TOTAL DE GOLS feitos durante o campeonato.

jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for g in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {g}? ')))
jogador['gols'] = partidas
jogador['total'] = sum(partidas)

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i}, fez {v} gols.')
print(f' => Foi um total de {jogador["total"]} gols.')
