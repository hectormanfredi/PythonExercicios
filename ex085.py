# Crie um programa onde o usuário possa digitar SETE VALORES NUMÉRICOS e cadastre-os em uma LISTA ÚNICA que
# mantenha separados os valores PARES E ÍMPARES. No final, mostre os valores pares e ímpares em ordem CRESCENTE.


# SOLUÇÃO OFERECIDA PELO PROFESSOR
num = [[], []]  # Aqui é possível declarar uma única lista e criar listas dentro dentro dela
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor:'))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Todos os números cadastrados: {num}')
num[0].sort()
print(f'Os números pares digitados foram {num[0]}')
num[1].sort()
print(f'Os números ímpares digitados foram {num[1]}')

# SOLUÇÃO HECTOR
valores = list()
impar = list()
par = list()
for v in range(1, 8):
    valores.append(int(input(f'Digite o {v}º valor:')))
    for n in valores:
        if n % 2 == 0:
            par.append(n)
        elif n % 2 == 1:
            impar.append(n)
    valores.clear()
print('-=' * 30)
par.sort()
valores.append(par[:])
impar.sort()
valores.append(impar[:])

print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')






