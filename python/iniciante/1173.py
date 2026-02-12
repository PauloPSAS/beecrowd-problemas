vetor = list()

n = int(input())
d = 0
for value in range(10):
    if value == 0:
        vetor.append(n)
        t = d
        d = n + t
        n = d
    else:
        t = d
        d = n + t
        n = d
        vetor.append(d)
    print(f"N[{value}] = {vetor[value]}")
