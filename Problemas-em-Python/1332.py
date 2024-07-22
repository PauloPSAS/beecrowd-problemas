qtd = int(input())

for x in range(qtd):
    txt = input().lower()

    if len(txt) > 3:
        print(3)
    else:
        soma = 0
        if txt[0:1] == 'o':
            soma += 1
        if txt[1:2] == 'n':
            soma += 1
        if txt[2:3] == 'e':
            soma += 1
        if soma >= 2:
            print(1)
        else:
            print(2)
