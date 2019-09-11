# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais
# - ESCALENO: todos os lados diferentes

rt1 = float(input('Digite o valor da primeira reta: '))
rt2 = float(input('Digite o valor da segunda reta: '))
rt3 = float(input('Digite o valor da terceira reta: '))

if (rt2 - rt3) < rt1 < rt2 + rt3 and (rt1 - rt3) < rt2 < rt1 + rt3 and (rt1 - rt2) < rt3 < rt1 + rt2:
    print('É possível formar um triângulo ', end='')  # o end='' significa que não terá a quebra da linha
    if rt1 == rt2 == rt3:
        print('EQUILÁTERO')
    elif rt1 == rt2 or rt1 == rt3 or rt2 == rt3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('This is impussibru!')


