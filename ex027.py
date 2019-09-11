# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

# colocando o -1 de posição irá contar de trás para frente

nome = str(input('Digite o seu nome completo: ')).strip()
dividido = nome.split()
print('primeiro nome: {}'.format(dividido[0]))
print('último nome: {}'.format(dividido[-1]))
# print('último nome: {}'.format(dividido[len(dividido) - 1]))
