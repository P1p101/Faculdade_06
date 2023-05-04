# Captura dois números e imprime com format ().
num1 = int(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
soma = num1+num2
print('Tipo do primeiro número: ', type(num1))
print('Tipo do segundo número:', type(num2))
print('\n A soma entre {0} e {1} é {2}'.format(num1, num2, soma))
print('\nO tipo da soma é: ', type(soma))