while True:
    a, b = map(str, input().split())

    soma = int(a) + int(b)
    if a == '0' and b == '0':
        break
    for l in str(soma):
        if l != '0':
            print(l, end='')
    print()
