# Captura um número e verifica se é primo.
num = int(input('Digite um número para ver se é primo: '))
i = 2
while i < num:
    if num % i == 0:
        print(num, 'Esse número NÃO É PRIMO!')
        break
    i += i
else:
    print(num, 'Esse número É PRIMO')