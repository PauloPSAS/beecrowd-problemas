# Matriz Quadrada II

ordem = int(input())

while ordem != 0:
    for i in range(1, ordem + 1):
        for j in range(1, ordem + 1):
            valor = abs(i - j) + 1
            if j == 1:
                print(f"{valor:>3}", end='')
            else:
                print(f" {valor:>3}", end='')
        print()
    ordem = int(input())
    if ordem != 0:
        print()
