listaNum = list()
pares = 0
for n in range(0, 5):
    listaNum.append(int(input()))
    if listaNum[n] % 2 == 0:
        pares += 1
print(f"{pares} valores pares")
