casos = int(input())

for i in range(casos):
    x, y = map(int, input().split())

    contador = total = 0

    while contador < y:
        if x % 2 != 0:
            total += x
            contador += 1
            x += 1
        else:
            x += 1
    print(total)
