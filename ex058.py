# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
# vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
pc = randint(0, 10)
print('Acabei de pensar em um número de 0 a 10, em qual número eu pensei? ')
c = 1
jogador = int(input('Digite um número: '))
while jogador != pc:
    if jogador < pc:
        print('Mais...', end='')
        jogador = int(input('Tente novamente: '))
    else:
        print('Menos...', end='')
        jogador = int(input('Tente novamente:'))
    c = c + 1
print('Você acertou! Eu pensei no número {}'.format(pc))
print('TOTAL DE TENTATIVAS: {}'.format(c))
"""

from random import randint
pc = randint(0, 10)
acertou = False
print('Pensei em um número de 0 a 10, em qual número que eu pensei?')
palpite = 0
while not acertou:
    jogador = int(input('Digite um número: '))
    palpite = palpite + 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente novamente. ', end='')
        else:
            print('Menos... Tente novamente. ', end='')
print('Você acertou com {} palpites.'.format(palpite))

