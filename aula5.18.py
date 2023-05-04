# Captura um número e imprime a tabuada.
num = int(input('Digite um número para ver a sua tabuada: '))
for i in range(1,11):
    print(num, 'x', i, '=', num*i)
    resultado = int(num * i)
    print('{0} x {1} = {2}'.format(num, i, resultado))