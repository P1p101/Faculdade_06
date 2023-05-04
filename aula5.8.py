# Calcula fahrenheit e celsius.
celsius = float(input('Digite a temperatura em Cº: '))
while celsius < -273.15:
    celsius = float(input('Valor inválido! Digite novamente: '))
fahrenheit = (celsius * 9/5) + 32
print(celsius, 'Cº é igual a', fahrenheit, 'Fº')