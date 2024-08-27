X = int(input())
Z = int(input())

while Z <= X:
    Z = int(input())

v = X
s = cont = 0
while s <= Z:
    s += v
    v += 1
    cont += 1
print(cont)
