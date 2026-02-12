# Número Perfeito

casos = int(input())

for i in range(1, casos+1):
    valor = int(input())
    divisivel = []
    for j in range(1, valor):
        if valor % j == 0:
            divisivel.append(j)

    if sum(divisivel) == valor:
        print("{} eh perfeito".format(valor))
    else:
        print("{} nao eh perfeito".format(valor))
