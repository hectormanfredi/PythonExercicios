# Crie um programa que faça o computador jogar JOKENPÔ COM VOCÊ.

from random import choice
from time import sleep
cores = {'limpa': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'azul': '\033[1;34m'}
player1 = str(input('Jokeennnpô:\n'
                    '- Pedra\n'
                    '- Papel\n'
                    '- Tesoura\n'
                    'Escreva a opção desejada: ')).strip().capitalize()
print('JO', end='')
sleep(1)
print('KEN', end='')
sleep(1)
print('PÔ!')
sleep(1)
pc = choice(['Pedra', 'Papel', 'Tesoura'])
# Verificando se o usuário digita a opção correta, se True entrará no if abaixo, se não irá direto para o else
if player1 == 'Pedra' or player1 == 'Papel' or player1 == 'Tesoura':
    # Opções para o player1 vencer
    if player1 == pc:
        print('O jogo deu {}EMPATE{}\n'
              'Player1 - {}\n'
              'Pc - {}'.format(cores['azul'], cores['limpa'], player1, pc))
    elif player1 == 'Pedra' and pc == 'Tesoura':
        print('O VENCEDOR É Player1 pois Pedra ganha de Tesoura\n'
              '{}VENCEDOR Player1 - {}{}\n'
              '{}PERDEDOR Pc - {}{}'
              .format(cores['verde'], player1, cores['limpa'], cores['vermelho'], pc, cores['limpa']))
    elif player1 == 'Tesoura' and pc == 'Papel':
        print('O VENCEDOR É Player1 pois Tesoura ganha de Papel\n'
              '{}VENCEDOR Player1 - {}{}\n'
              '{}PERDEDOR Pc - {}{}'
              .format(cores['verde'], player1, cores['limpa'], cores['vermelho'], pc, cores['limpa']))
    elif player1 == 'Papel' and pc == 'Pedra':
        print('O VENCEDOR É Player1 pois Papel ganha de Pedra\n'
              '{}VENCEDOR Player1 - {}{}\n'
              '{}PERDEDOR Pc - {}{}'
              .format(cores['verde'], player1, cores['limpa'], cores['vermelho'], pc, cores['limpa'],))

    # Opções para o computador vencer
    elif pc == 'Pedra' and player1 == 'Tesoura':
        print('O VENCEDOR É PC, pois Pedra ganha de Tesoura\n'
              '{}VENCEDOR Pc - {}{}\n'
              '{}PERDEDOR Player1 - {}{}'
              .format(cores['verde'], pc, cores['limpa'], cores['vermelho'], player1, cores['limpa']))
    elif pc == 'Tesoura' and player1 == 'Papel':
        print('O VENCEDOR É PC, pois Tesoura ganha de Papel\n'
              '{}VENCEDOR Pc - {}{}\n'
              '{}PERDEDOR Player1 - {}{}'
              .format(cores['verde'], pc,  cores['limpa'], cores['vermelho'], player1, cores['limpa']))
    elif pc == 'Papel' and player1 == 'Pedra':
        print('O VENCEDOR É PC, pois Papel ganha de Pedra\n'
              '{}VENCEDOR Pc - {}{}\n'
              '{}PERDEDOR Player1 - {}{}'
              .format(cores['verde'], pc, cores['limpa'], cores['vermelho'], player1, cores['limpa']))

    # Nenhuma das seis opções acima, rever o código.
    else:
        print('Tem alguma coisa errada no código\n'
              'Pc - {}\n'
              'Player1 - {}'.format(pc, player1))

else:
    print('Erro! Opção inválida! Tente novamente')

