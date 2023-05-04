# APS1:
nota1 = float(input('Digite a nota do primeiro bimestre: '))
nota2 = float(input('Digite a nota do segundo bimestre: '))
nota3 = float(input('Digite a nota do terceiro bimestre: '))
nota4 = float(input('Digite a nota do quarto bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print('A nota primeiro bimestre é: ', nota1)
print('A nota do segundo bimestre é: ', nota2)
print('A nota do terceiro bimestre é: ', nota3)
print(('A nota do quarto bimestre é: ', nota4))
print('A média final é: ', media)

if media >= 70:
    print('Aluno(a) Aprovado(a)!')
elif media < 40:
    print('Aluno(a) Reprovado(a).')
else:
    exame_final = float(input('Digite a nota do exame final: '))
    nova_media = (media + exame_final) / 2
    if nova_media >= 50:
        print('Aluno(a) Aprovado(a)!')
    else:
        print('Aluno(a) Reprovado(a) no exame final.')
