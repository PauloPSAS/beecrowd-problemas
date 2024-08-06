def soma_nao_multiplos_de_13(X, Y):
    if X > Y:
        X, Y = Y, X
    
    soma = 0
    for i in range(X, Y + 1):
        if i % 13 != 0:
            soma += i
    
    return soma

X = int(input())
Y = int(input())

resultado = soma_nao_multiplos_de_13(X, Y)
print(resultado)
