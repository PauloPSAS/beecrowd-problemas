N = int(input())

for x in range(1, N+1):
    print(x, end=' ')
    print(x * x, end=' ')
    print((x * x) * x)

    print(x, end=' ')
    print((x * x) + 1, end=' ')
    print(((x * x) * x) + 1)
    