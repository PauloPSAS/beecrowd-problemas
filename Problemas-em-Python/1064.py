numeros = []
positivos = media = 0
for num in range(0, 6):
    numeros.append(float(input()))
    if numeros[num] > 0:
        positivos += 1
        media += numeros[num]


print(f"{positivos} valores positivos")
print(f"{media / positivos :.1f}")
