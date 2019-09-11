# Crie um programa onde o usuário possa digitar cinco VALORES NÚMERICOS e cadastre-os em uma LISTA,
# já na posição correta de inserção (sem usar o sort()).
# No final, mostre a LISTA ORDENADA na tela.

valores = list()
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > valores[-1]:
        valores.append(num)
    else:
        pos = 0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos, num)
                break
            pos = pos + 1
print(f'Os valores digitados em ordem foram: {valores}')


# NÃO CONSEGUI FAZER




