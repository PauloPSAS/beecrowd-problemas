casos = int(input())

for x in range(casos):
    v1, v2 = map(str , input().split())
    if v1.endswith(v2):
        print("encaixa")
    else:
        print("nao encaixa")