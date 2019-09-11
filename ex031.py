# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50
# por KM para viagens de até 200km e R$0,45 para viagens mais longas.

dist = int(input('Digite a distância de sua viagem em Km: '))
if dist <= 200:
    p = dist * 0.50
    print('A sua viagem é de até 200km e sua passagem custa R${:.2f}.'.format(p))
else:
    p = dist * 0.45
    print('A sua viagem tem {}Km e sua passagem custa R${:.2f}'.format(dist, p))
print('Tenha uma boa viagem!')

