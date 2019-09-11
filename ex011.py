# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

# largura x altura

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
qtdtinta = area / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².'.format(l, a, area))
print('Para pintar essa parede é preciso de {:.1f}l de tinta.'.format(qtdtinta))
