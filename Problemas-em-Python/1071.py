v1 = int(input())
v2 = int(input())
soma = 0

if v1 > v2:
    for x in range(v2+1, v1):
        if x % 2 != 0:
            soma += x

else:
    for x in range(v1+1, v2):
        if x % 2 != 0:
            soma += x

print(soma)