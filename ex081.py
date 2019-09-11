# Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma lista.
# Depois disso, mostre:

# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma DECRESCENTE.
# C) Se o valor 5 foi digitado e está ou não na LISTA.

valores = list()

while True:
    # valores.append(int(input('Digite um valor: ')))
    num = int(input('Digite um valor:'))
    valores.append(num)
    opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]: ')).upper()[0]
    if opcao == 'N':
        break
print('-=' * 30)
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'A lista ordenada de forma decrescente é: {valores}')
if 5 in valores:
    for i, v in enumerate(valores):
        if v == 5:
            print(f'O 5 está na lista na posição {i}')
else:
    print('O 5 não está na lista')


