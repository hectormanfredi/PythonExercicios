# Crie um programa onde 4 JOGADORES joguem um DADO e tenham resultados ALEATÓRIOS. Guarde esses resultados em um
# DICIONÁRIO. No final, coloque esse dicionário em ORDEM, sabendo que o VENCEDOR tirou o MAIOR NÚMERO no dado.

from random import randint
from time import sleep
# Com essa biblioteca é possivel pegar um item, no caso a posição da lista
from operator import itemgetter

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}

print('VALORES SORTEADOS: ')
ranking = list()
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
# Aqui for preciso ordenar a lista com o método sorted, jogando dentro dele todos os items do dicionário jogos,
# ordenando pelo indice 1 com o método itemgetter da biblioteca operator, e ordenando do maior para o menor.
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}')




