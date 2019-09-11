# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e a raiz quadrada

n = int(input('Digite um número: '))
print('O dobro de {} é {}.\n O triplo de {} é {}.\n E a raiz quadrada de {} é {:.2f}.'
      .format(n, n * 2, n, n * 3, n, pow(n, (1/2))))
