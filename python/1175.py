lista = list()

for v in range(20):
    n = int(input())
    lista.append(n)

lista.reverse()
for v in range(len(lista)):
    print(f"N[{v}] = {lista[v]}")
    