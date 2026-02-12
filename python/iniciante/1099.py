n = int(input())

for v in range(n):
    x, y = map(int, input().split())

    s = 0
    if x > y:
        if y % 2 != 0:
            y += 1
        for c in range(y, x):
            if c % 2 != 0:
                s += c
    elif y > x:
        if x % 2 != 0:
            x += 1
        for c in range(x, y):
            if c % 2 != 0:
                s += c
    else:
        s = 0
    print(s)
