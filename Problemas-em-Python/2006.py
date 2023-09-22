t = input()
r = 0
a, b, c, d, e = input().split()

lista = a, b, c, d, e

for i in lista:
    if i == t:
        r += 1
print(r)
