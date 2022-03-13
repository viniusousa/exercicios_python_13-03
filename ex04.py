'''
4) Crie um script em Python que receba vários números do usuário e os armazene em uma
lista. Depois, o algoritmo deve imprimir todos os números contidos na lista em ordem
crescente.
'''

qt = int(input('Digite quantos numero deseja inserir:  '))

lista = []

for c in range(1, qt + 1):
    valor = int(input(f'Insira o {c}° valor: '))
    lista.append(valor)

print(sorted(lista))

