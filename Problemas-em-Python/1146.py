def seq(x):
    for v in range(1, x+1):
        if v != x:
            print(v, end=' ')
        else:
            print(v)

while True:
    v = int(input())

    if v != 0:
        seq(v)
    else:
        break
    