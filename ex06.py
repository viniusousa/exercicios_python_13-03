'''
6) Crie um algoritmo que receba do usuário as supostas médias de uma determinada turma
de alunos. Depois o algoritmo deve retornar:
a) Média geral da turma
b) Menor média
c) Maior média
'''

medias = []
qt = int(input('Insira a quantidade alunos: '))

for c in range(1, qt +1):
    media = float(input(f'Insira a média do {c}° Aluno: '))
    medias.append(media)


print(f'A média total das notas é {(sum(medias)) / qt :.2f}')
print('-' * 25)
print(f'A menor média é {min(medias):.2f}')
print('-' * 25)
print(f'A maior média é {max(medias):.2f}')