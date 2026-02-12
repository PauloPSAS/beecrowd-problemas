N = int(input())
contador = 1

while contador <= N * 4:
    for i in range(3):
        if contador > N * 4:
            break
        print(contador, end=' ')
        contador += 1
    print("PUM")
    contador += 1
