celsius = float(input('Digite em graus Celsius: '))
while celsius < -273.15:
    celsius = float(input('Valor inválido'))
fahrenheit = (celsius * 9/5) + 32
print(celsius, 'Graus Celsius é igual a:',
    fahrenheit, 'Graus Fahrenheit')