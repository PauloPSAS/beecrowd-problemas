X = int(input())
Z = int(input())

while Z <= X:
    Z = int(input())

total = X
soma = cont = 0
while soma <= Z:
    soma += total
    total += 1
    cont += 1
print(cont)
