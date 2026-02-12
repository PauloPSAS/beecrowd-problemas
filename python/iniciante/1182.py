def soma(c, m):
    soma = 0
    for linha in m:
        soma += linha[c]
    return soma


def media(c, m):
    media = cont = 0
    for linha in m:
        if linha[c] != 0:
            media += linha[c]
            cont += 1
    return media / cont


matriz = [[0 for i in range(12)] for j in range(12)]

C = int(input())

caractere = input().upper()

for lista in range(12):
    for coluna in range(12):
        matriz[lista][coluna] = float(input())

if caractere == 'S':
    print(f"{soma(C, matriz):.1f}")

elif caractere == 'M':
    print(f"{media(C, matriz):.1f}")
