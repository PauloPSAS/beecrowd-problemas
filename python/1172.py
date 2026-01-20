vetor = list()
for x in range(10):
    vetor.append(int(input()))
    if vetor[x] <= 0:
        vetor.pop()
        vetor.append(1)
    print(f"X[{x}] = {vetor[x]}")
