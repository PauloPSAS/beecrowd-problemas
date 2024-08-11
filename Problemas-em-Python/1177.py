t = int(input())

contador = 0
for v in range(1000):
    print("N[{}] = {}".format(v, contador))
    if contador == t-1:
        contador = 0
    else:
        contador += 1
