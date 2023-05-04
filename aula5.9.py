# Captura duas notas e imprime as notas e a média.
nome = input('Digite o seu nome: ')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota:'))
media = (nota1+nota2)/2
msg = ('Olá {0} Primeira nota {1} Segunda nota {2} média {3}'
       .format(nome, nota1, nota2, media))
print(msg)
