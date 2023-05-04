# Captura 10 notas de alunos e calcula a média da turma.
soma = 0
i = 1
while i <= 5:
    nota = float(input('Digite a nota do aluno: '))
    soma += nota
    i += 1
media = soma / 10
print('A média da turma é: ', media)
print('A média da turma é: {0}'.format(media))
print(f'A média da turma é: {media}')
