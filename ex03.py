'''
3) Crie um algoritmo que receba do usuário um número. Depois, o algoritmo deve retornar
se o número é ou não um número primo. Por fim, utilizando listas, caso o número não seja
primo, o algoritmo deve armazenar todos os divisores dele e imprimí-los na tela.
'''

num = int(input('Insira um número: '))

lista = []

for c in range (1, num +1):
    if num % c ==0:
        lista.append(c)

if len(lista) == 2:
    print(f'{num} é um número primo!')
else: 
    print(f'{num} não é um número primo! ')
    print(f'Seus divisores são: {lista} ')


