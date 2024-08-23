def soma(l, m):
    soma = 0
    for v in m[l]:
        soma += v
    return soma

def media(l, m):
    media = cont = 0
    for v in m[l]:
        if v == 0:
            continue
        else:
            media += v
            cont += 1
    return media / cont
        


matriz = [[0 for i in range(12)] for j in range(12)]

L = int(input())

caractere = input().upper()


for lista in range(12):
    for coluna in range(12):
        matriz[lista][coluna] = float(input())

if caractere == 'S':
    print(f"{soma(L, matriz):.1f}")

elif caractere == 'M':
    print(f"{media(L, matriz):.1f}")
