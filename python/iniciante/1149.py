valores = list(map(int, input().split()))

A = valores[0]
for i in valores[1:]:
    if i > 0:
        I = i
        break

s = 0
for x in range(I):
    s += A+x
print(s)
