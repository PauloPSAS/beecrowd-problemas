p1, c1, p2, c2 = map(int, input().split())

lDireito = p2 * c2
lEsquerdo = p1 * c1

if lDireito == lEsquerdo:
    print(0)
elif lDireito < lEsquerdo:
    print(-1)
else:
    print(1)
