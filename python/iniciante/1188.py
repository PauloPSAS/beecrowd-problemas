def area_inferior(m):
    valoresSuperiores = []
    n = len(m)
    for i in range(n):
        for j in range(n):
            if i > j and i + j > n - 1:
                valoresSuperiores.append(m[i][j])
    return valoresSuperiores


def media(m):
    c = s = 0
    for x in m:
        if m != 0:
            s += x
            c += 1
    return s / c


O = input().strip().upper()

matriz = [[0 for _ in range(12)] for _ in range(12)]

for l in range(12):
    for e in range(12):
        matriz[l][e] = float(input())

valoresSuperiores = area_inferior(matriz)

if O == 'S':
    t = sum(valoresSuperiores)
elif O == 'M':
    t = media(valoresSuperiores)

print(f'{t:.1f}')
