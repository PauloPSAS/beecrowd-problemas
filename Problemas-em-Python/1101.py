
while True:
    soma = 0
    a, b = map(int, input().split())

    if a <= 0 or b <= 0:
        break

    elif a > b:
        for x in range(b, a + 1):
            print(x, end=' ')
            soma += x
    
    else:
        for x in range(a, b + 1):
            print(x, end=' ')
            soma += x
    
    print(f"Sum={soma}")
