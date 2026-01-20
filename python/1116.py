n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    if y == 0:
        print("divisao impossivel")
    else:
        quociente = x / y
        print(f"{quociente:.1f}")
        