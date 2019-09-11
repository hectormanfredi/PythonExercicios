# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
soma = 0
multiplicar = 0
opcao = 0
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
while opcao != 5:
    opcao = int(input('''O que você deseja fazer:
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
>>>>>>> Digite sua opção: '''))
    if opcao == 1:
        print('Você escolheu a opção {} de soma'.format(opcao))
        soma = num1 + num2
        print('Então {} + {} é igual a {}'.format(num1, num2, soma))
    elif opcao == 2:
        print('Você escolheu a opção {} de multiplicar'.format(opcao))
        multiplicar = num1 * num2
        print('Então {} * {} é igual a {}'.format(num1, num2, multiplicar))
    elif opcao == 3:
        print('Você escolheu a opção {} de maior'.format(opcao))
        if num1 > num2:
            print('Então o número {} é maior que o número {}'.format(num1, num2))
        else:
            print('Então o número {} é maior que o número {}'.format(num2, num1))
    elif opcao == 4:
        print('Você escolheu a opção {} de novos números.'.format(opcao))
        num1 = int(input('Digite um novo número: '))
        num2 = int(input('Digite o segundo novo número: '))
    else:
        opcao not in(1, 2, 3, 4, 5)
        print('Opção inválida, tenta novamente!')
    print('=-=' * 10)
print('Finalizando...')
sleep(2)
print('Programa finzaliado com sucesso!')
