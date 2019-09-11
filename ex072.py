# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num = int(input('Digite um número de 0 até 20: '))
tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
         'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    if num > 20 or num < 0:
        num = int(input('Valor inválido. Digite um número de 0 até 20: '))
    else:
        for c in range(0, len(tupla)):
            if num == c:
                print(f'Você digitou o número {tupla[c]}')
        break
        # É possível também fazer conforme a forma abaixo:
        # for pos, cont in enumerate(tupla):
        #     if num == pos:
        #         print(f'você digitou {tupla[pos]}')

