# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.
v = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(v)))
print('Só tem espaços? {}'.format(v.isspace()))
print('É um número? {}'.format(v.isnumeric()))
print('É alfabético? {}'.format(v.isalpha()))
print('Está em maiúsculas? {}'.format(v.isupper()))
print('Está em minúsculas? {}'.format(v.islower()))
print('Está capitalizada? {}'.format(v.istitle()))
