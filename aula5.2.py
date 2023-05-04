# APS2:
num = int(input('Digite um número para ver se é primo: '))
i = 2
while i < num:
    if num % i == 0:
        print(num, 'Esse número não é PRIMO!')
        break
    i += 1
else:
    print(num, 'Esse número é PRIMO!')