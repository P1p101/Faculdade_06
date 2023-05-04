# Captura um número e informa se é par ou impar.
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print('O', num, 'par')
else:
    print('O', num, 'é impar')