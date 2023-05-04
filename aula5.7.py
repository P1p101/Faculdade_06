# Captura a idade e informa se é criança, adolescente, adulto ou idoso.
idade = int(input('Digite sua idade: '))
if idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
elif idade < 60:
    print('Adulto')
else:
    print('Idoso')