'''
5) Número natural perfeito é aquele que é igual a soma de todos os seus fatores (divisores).
Como exemplo podemos citar o número 6 (6 = 3 + 2 + 1). Crie um algoritmo que contenha
que receba um número e imprima no terminal se ele é ou não um número perfeito.
'''

numero = int(input('Insira o número: '))

limite = int(numero / 2)
total = 0

if numero != 0 and numero != 1:
    total = 1

if numero % 2 == 0:
    total += limite + 2

for c in range(3, limite):
    if numero % c == 0:
        total += c

#fazer a verificação
if numero == total:
    print('Número Perfeito!')
else:
    print('Número não perfeito!')