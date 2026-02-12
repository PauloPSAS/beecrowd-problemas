casos = int(input())

for x in range(casos):
    a, b = input().split()
    resultado = []

    tamanho = max(len(a), len(b))

    for x in range(tamanho):
        if x < len(a):
            resultado.append(a[x])
        if x < len(b):
            resultado.append(b[x])
    print("".join(resultado))
