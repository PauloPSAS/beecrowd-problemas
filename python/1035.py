valores = input().split()
v1, v2, v3, v4 = valores

if int(v2) > int(v3) and int(v4) > int(v1) and int(v3) + int(v4) > int(v1) + int(v2) and int(v3) and int(v4) > 0 and \
        int(v1) % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
