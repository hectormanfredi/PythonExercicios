# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
cont = 0
while True:
    soma = 0
    pc = randint(1, 10)
    # print(f'pc = {pc}')
    opcao = ' '
    jogador = int(input('Diga um valor: '))
    while opcao not in 'PI':
        opcao = str(input('Você quer PAR ou ÍMPAR [P/I]: ')).upper().strip()[0]
        print('-' * 50)
    if opcao == 'P':
        soma = jogador + pc
        if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} DEU PAR')
            print('-' * 50)
            print('Você ganhou! Vamos jogar novamente...')
            cont = cont + 1
        else:
        #if soma % 2 != 0:
            print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} DEU ÍMPAR')
            print('-' * 50)
            print('Você PERDEU!')
            break
    if opcao == 'I':
        soma = jogador + pc
        if soma % 2 != 0:
            print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} DEU IMPAR')
            print('-' * 50)
            print('Você ganhou! Vamos jogar novamente...')
            cont = cont + 1
        else:
        #if soma % 2 == 0:
            print(f'Você jogou {jogador} e o computador {pc}. Total de {soma} DEU PAR')
            print('-' * 50)
            print('Você PERDEU!')
            break
print('-' * 50)
print(f'GAME OVER! Você venceu {cont} vezes.')

