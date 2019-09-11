# Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema de visualização de
# DETALHES DE APROVEITAMENTO de cada jogador.

# Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai ler o NOME DO JOGADOR e
# QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso será
# guardado em um dicionário, incluindo o TOTAL DE GOLS feitos durante o campeonato.

time = list()
jogador = dict()
partidas = list()
while True:
    # AQUI É PRECISO LIMPAR O DICIONÁRIO PARA QUE ELE NÃO ACUMULE
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    """ AQUI É PRECISO LIMPAR A LISTA PARTIDAS PARA QUANDO CADASTRAR UM NOVO JOGADOR NÃO ACUMULAR AS PARTIDAS DO JOGADOR
    ANTERIOR """
    partidas.clear()
    for p in range(0, total):
        partidas.append(int(input(f'Quantos gols na partida {p}? ')))
    """AQUI É FEITO A CÓPIA DA LISTA PARTIDAS PARA A CHAVE GOLS DO DICIONARIO
    JOGADOR POR FATIAMENTO TOTAL DA LISTA PARTIDAS"""
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())
    op = str(input('Quer continuar? [S/N] '))
    if op in 'Nn':
        break

print('-' * 40)
print(f'cod ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()

for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('-' * 40)


while True:
    op = int(input('Mostrar dados de qual jogador? (999 para sair)'))
    if op == 999:
        break
    if op >= len(time):
        print('JOGAR NÃO EXISTE, tente novamente!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[op]["nome"]}:')
        for i, g in enumerate(time[op]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')





