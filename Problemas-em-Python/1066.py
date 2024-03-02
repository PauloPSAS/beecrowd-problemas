values = []
par = impar = negativo = positivo = 0
for n in range(5):
    values.append(int(input()))
    if values[n] % 2 == 0:
        par += 1
    else:
        impar += 1
    if values[n] > 0:
        positivo += 1
    else:
        negativo += 1
print(f"{par} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")
