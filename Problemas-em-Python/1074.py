def positivo():
    print("POSITIVE")


def negativo():
    print("NEGATIVE")


n = int(input())

for x in range(n):
    num = int(input())

    if num == 0: # Se é 0(zero)
        print("NULL")

    elif num % 2 == 0: # Se é par
        print("EVEN", end=' ')
        if num < 0:
            negativo()
        else:
            positivo()
    
    else: # Senão é ímpar
        print("ODD", end=' ')
        if num > 0:
            positivo()
        else:
            negativo()
