def resto(X, Y):
    if X > Y:
        X, Y = Y, X

    for i in range(X+1, Y):
        if i % 5 == 2 or i % 5 == 3:
            print(i)


x = int(input())
y = int(input())
resto(x, y)
