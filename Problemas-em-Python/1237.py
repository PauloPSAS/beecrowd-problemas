import sys

entrada = sys.stdin.read().splitlines()

i = 0
while i < len(entrada) - 1:
    frase1 = entrada[i]
    frase2 = entrada[i + 1]
    i += 2

    len1 = len(frase1)
    len2 = len(frase2)

    matriz_comprimentos = []
    for x in range(len1 + 1):
        linha = []
        for y in range(len2 + 1):
            linha.append(0)
        matriz_comprimentos.append(linha)

    comprimento_maximo = 0

    for x in range(len1):
        for y in range(len2):
            if frase1[x] == frase2[y]:
                matriz_comprimentos[x + 1][y + 1] = matriz_comprimentos[x][y] + 1
                if matriz_comprimentos[x + 1][y + 1] > comprimento_maximo:
                    comprimento_maximo = matriz_comprimentos[x + 1][y + 1]

    print(comprimento_maximo)
