qtd = int(input())
values = list()
i = j = 0
for n in range(0, qtd):
    values.append(int(input()))
    if 20 >= values[n] >= 10:
        i += 1
    else:
        j += 1
print(f"{i} in")
print(f"{j} out")
