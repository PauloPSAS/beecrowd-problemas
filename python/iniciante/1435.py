while True:
    N = int(input())

    # Se digitar 0, encerra o código.
    if N == 0:
        break

    matriz = [[1] * N for _ in range(N)]  # Inicializa a matriz com todos os elementos sendo 1.

    # Determina o número de camadas que terá a matriz
    camadas = (N + 1) // 2

    # Preenche as camadas da matriz
    for camada in range(1, camadas):
        for i in range(camada, N - camada):
            for j in range(camada, N - camada):
                matriz[i][j] = camada + 1

    # Imprime a matriz com a formatação correta
    for linha in range(N):
        for col in range(N):
            if col < (N - 1):
                print(f"{matriz[linha][col]:>3}", end=" ")
            else:
                print(f"{matriz[linha][col]:>3}")
    print()
