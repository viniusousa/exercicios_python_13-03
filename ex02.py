'''
2) Faça um programa que carregue um dicionário com os modelos de cinco carros (exemplo
de modelos: FUSCA, GOL, VECTRA etc) e o consumo de cada um deles, isto é, quantos
quilômetros cada um desses carros faz com um litro de combustível. Depois, calcule e
mostre:
a) O modelo do carro mais econômico;
b) Quantos litros de combustível cada um dos carros cadastrados consome para
percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando
um que a gasolina custe R$ 6,25 o litro.
'''

from operator import itemgetter

#o modelo e quanto o carro faz por litro

carros = [
     {'modelo': 'Chevrolet Onix', 'consumo': 16.7},
     {'modelo': 'Hyundai HB20S', 'consumo': 13.6},
     {'modelo': 'Fiat Argo', 'consumo': 17.2},
     {'modelo': 'Fiat Cronos', 'consumo': 16},
     {'modelo': 'Renault Logan', 'consumo': 14.2}
]

# Ordenando pelo carro que faz mais km por litro, consequentemento o mais economico.

carros_porconsu = sorted(carros, key=itemgetter('consumo'), reverse=True)


print(f'O modelo mais econômico é {carros_porconsu[0]["modelo"]}, fazendo {carros_porconsu[0]["consumo"]}km/L.')
print('--' * 20)
print('Considerando uma distancia de 1000km e a Gasolina a R$: 6,25 o litro o consumo dos carros resulta em: ')

for c in range(0, len(carros)):
     print(f'{carros_porconsu[c]["modelo"]}, gasto de {1000 / carros_porconsu[c]["consumo"]:.2f}L e R$:{(1000 / carros_porconsu[c]["consumo"]) * 6.25:.2f}')











