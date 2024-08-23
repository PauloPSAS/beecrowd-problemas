def media_matriz(m):
    media = cont = 0
    for y in range(12):
        for z in range(12):
            if y > z:
                media += m[y][z]
                cont += 1
    return media / cont if cont != 0 else 0


def soma_matriz(m):
    soma = 0
    for y in range(12):
        for z in range(12):
            if y > z:
                soma += m[y][z]
    return soma


matriz = [[0 for _ in range(12)] for _ in range(12)]

O = input().upper()

for i in range(12):
    for j in range(12):
        matriz[i][j] = float(input().upper())

if O == 'S':
    s = soma_matriz(matriz)
elif O == 'M':
    s = media_matriz(matriz)

print(f"{s:.1f}")
