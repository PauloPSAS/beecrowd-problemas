casos = int(input())
notas = list()
medias = list()

for x in range(1, casos+1):
    notas = list(map(float, input().split()))
    medias.append(((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 5)) / (2 + 3 + 5))

for x in range(0, casos):
    print(f"{medias[x]:.1f}")
