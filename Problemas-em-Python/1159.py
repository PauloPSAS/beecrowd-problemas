# Soma de 5 pares consecutivos

valor_entrada = int(input())
while valor_entrada != 0:
    soma = 0
    for _ in range(valor_entrada, valor_entrada + 10):
        if _ % 2 == 0:
            soma += _
    print(soma)
    if valor_entrada != 0:
        valor_entrada = int(input())
