soma = 0
while True:
    m, n = map(int, input().split())
    soma = 0
    if m > n:
        aux = m
        m = n
        n = aux
    if m <= 0 or n <= 0:
        break

    if True:
        for i in range(m, n+1):
            print(i, end=' ')
            soma+=i
        print(f"Sum={soma}")
    