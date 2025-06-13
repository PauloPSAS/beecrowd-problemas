import sys

for frase1 in sys.stdin:
    frase1 = frase1.strip()

    if not frase1:
        continue

    try:
        frase2 = input()

        len1 = len(frase1)
        len2 = len(frase2)

        matriz_comprimentos = [[0] * len2 + 1 for _ in range(len1 + 1)]

        comprimento_maximo = 0

        # Preenche a matriz com os tamanhos das substrings comuns
        for i in range(len1):
            for j in range(len2):
                if frase1[i] == frase2[j]:
                    matriz_comprimentos[i+1][j+1] = matriz_comprimentos[i][j] + 1

                    if matriz_comprimentos[i+1][j+1] > comprimento_maximo:
                        comprimento_maximo = matriz_comprimentos[i+1][j+1]

        print(comprimento_maximo)
    
    except Exception as e:
        break
