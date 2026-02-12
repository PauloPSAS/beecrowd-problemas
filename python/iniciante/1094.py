repeat = int(input())
totalCobaias = totalC = totalR = totalS = 0

for x in range(repeat):
    qtd, tipe = map(str, input().split())

    qtd = int(qtd)
    tipe = tipe.upper()
    totalCobaias += qtd

    if tipe == 'C':
        totalC += qtd
    elif tipe == 'R':
        totalR += qtd
    elif tipe == 'S':
        totalS += qtd

print(f"Total: {totalCobaias} cobaias")
print(f"Total de coelhos: {totalC}")
print(f"Total de ratos: {totalR}")
print(f"Total de sapos: {totalS}")
print(f"Percentual de coelhos: {totalC / totalCobaias * 100:.2f} %")
print(f"Percentual de ratos: {totalR / totalCobaias * 100:.2f} %")
print(f"Percentual de sapos: {totalS / totalCobaias * 100:.2f} %\n")
