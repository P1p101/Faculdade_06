# Captura dois números e compara qual é maior.
num1 = int(input('Digite o primeiro número:'))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(num1, 'é maior que', num2)
elif num2 > num1:
    print(num2, 'é maior que ', num1)
else:
    print('Os dois números são iguais!')