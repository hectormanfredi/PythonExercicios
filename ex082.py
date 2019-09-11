# Crie um programa que vai ler VÁRIOS NÚMEROS e colocar em uma LISTA.
# Depois disso, crie DUAS LISTAS EXTRAS que vão conter apenas os valores PARES e os valores ÍMPARES digitados,
# respectivamente.

# Ao final, mostre o conteúdo das três listas geradas.

valores = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if opcao == 'N':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Os valores digitados foram: {valores}')
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
