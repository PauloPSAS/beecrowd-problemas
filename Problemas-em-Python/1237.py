import sys

for frase1 in sys.stdin:
    frase1 = frase1.strip()

    if not frase1:
        continue

    try:
        frase2 = input()

        len1 = len(frase1)
        len2 = len(frase2)

        comprimento_maximo = 0

        for inicio1 in range(len1):
            for fim1 in range(inicio1 + 1, len1 + 1):
                substring = frase1[inicio1:fim1]

                if substring in frase2:
                    tamanho = fim1 - inicio1

                    if tamanho > comprimento_maximo:
                        comprimento_maximo = tamanho

        print(comprimento_maximo)
    
    except Exception as e:
        break
