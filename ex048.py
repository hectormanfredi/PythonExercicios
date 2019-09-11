# Faça um programa que calcule a SOMA entre todos os NÚMEROS ÍMPARES que SÃO MÚLTIPLOS DE TRÊS e que se encontram no
# intervalo de 1 até 500.
s = 0
# Primeiro o FOR faz o intervalo de 1 até 500
for c in range(1, 500 + 1):
    # Neste if estou encontrando os números que são múltiplos de 3 e se True será armazenado em i
    if c % 3 == 0:
        i = c
        # Neste if estou procurando os números que são ÍMPARES e se True serão somados e armazeado a soma em s
        if i % 2 == 1:
            s = s + i
# Aqui eu imprimo a soma total de todos os números que são multiplos de 3 e que são ímpares
print('A soma dos números que são ímpares, múltiplos de 3 no intervalo de 1 até 500 é de: {}'.format(s))
