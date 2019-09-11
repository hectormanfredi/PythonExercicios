# Refaça o DESAFIO 009, mostrando a TABUADA de um número que o usuário escolher, só que agora utilizando um laço for.

v = int(input('Digite um número para ver a sua tabuada: '))
print('A tabuada do {} é :'.format(v))
for c in range(1, 10 + 1):
    tabuada = v * c
    print('{} x {} = {:<2} '.format(v, c, tabuada))
