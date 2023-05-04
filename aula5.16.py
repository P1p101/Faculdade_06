# Imprime a soma dos números entre 1 e 100.
soma = 0
i = 1
while i <= 100:
    soma += i
    i += 1
print('A soma de 1 a 100 é:', soma)
print('A soma de 1 a 100 é: {0}'.format(soma))
print(f'A soma de 1 a 100 é: {soma}')