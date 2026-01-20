valor = float(input())

nota_100 = valor // 100
valor = valor - nota_100 * 100

nota_50 = valor // 50
valor = valor - nota_50 * 50

nota_20 = valor // 20
valor = valor - nota_20 * 20

nota_10 = valor // 10
valor = valor - nota_10 * 10

nota_5 = valor // 5
valor = valor - nota_5 * 5

nota_2 = valor // 2
valor = valor - nota_2 * 2

moeda_1 = valor // 1
valor = valor - moeda_1 * 1
moeda_1 = float('%.2f' % moeda_1)
valor = float('%.2f' % valor)

moeda_50 = valor // 0.5
valor = valor - moeda_50 * 0.5
moeda_50 = float('%.2f' % moeda_50)
valor = float('%.2f' % valor)

moeda_25 = valor // 0.25
valor = valor - moeda_25 * 0.25
moeda_25 = float('%.2f' % moeda_25)
valor = float('%.2f' % valor)

moeda_10 = valor // 0.10
valor = valor - moeda_10 * 0.10
moeda_10 = float('%.2f' % moeda_10)
valor = float('%.2f' % valor)

moeda_5 = valor // 0.05
valor = valor - moeda_5 * 0.05
moeda_5 = float('%.2f' % moeda_5)
valor = float('%.2f' % valor)

moeda_01 = valor * 100
moeda_01 = float('%.2f' % moeda_01)
valor = float('%.2f' % valor)

print('NOTAS:')
print(f'{nota_100:.0f} nota(s) de R$ 100.00')
print(f'{nota_50:.0f} nota(s) de R$ 50.00')
print(f'{nota_20:.0f} nota(s) de R$ 20.00')
print(f'{nota_10:.0f} nota(s) de R$ 10.00')
print(f'{nota_5:.0f} nota(s) de R$ 5.00')
print(f'{nota_2:.0f} nota(s) de R$ 2.00')
print('MOEDAS:')
print(f'{moeda_1:.0f} moeda(s) de R$ 1.00')
print(f'{moeda_50:.0f} moeda(s) de R$ 0.50')
print(f'{moeda_25:.0f} moeda(s) de R$ 0.25')
print(f'{moeda_10:.0f} moeda(s) de R$ 0.10')
print(f'{moeda_5:.0f} moeda(s) de R$ 0.05')
print(f'{moeda_01:.0f} moeda(s) de R$ 0.01')
