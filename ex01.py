'''
1) Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima
a data com o nome do mês por extenso.
'''

meses = ["janeiro",
         "fevereiro",
         "março",
         "abril",
         "maio",
         "junho",
         "julho",
         "agosto",
         "setembro",
         "outubro",
         "novembro",
         "dezembro"]

data = input("informe sua data de nascimento (dd/mm/aaaa): ")


print (data.split("/")[0],
       "de",
       meses[(int(data.split("/")[1])-1)],
       "de",
       data.split("/")[2])

dia, mês, ano = input('Data (dd/mm/aaaa): ').split('/')
meses = ['janeiro','fevereiro','março','abril',
         'maio','junho','julho','agosto','setembro',
         'outubro','novembro','dezembro']
print ('Você nasce em:')
print (f'{dia} de {meses[int(mês) - 1]} de {ano}')
