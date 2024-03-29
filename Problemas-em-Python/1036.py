valores = input().split()

a, b, c = valores
a = float(a)
b = float(b)
c = float(c)
delta = (b ** 2 - 4 * a * c)

if a == 0.0 or delta < 0:
    print('Impossivel calcular')
else:
    x1 = (- b + (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    x2 = (- b - (b ** 2 - 4 * a * c) ** (1 / 2)) / (2 * a)
    print(f'R1 = {x1:.5f}')
    print(f'R2 = {x2:.5f}')
