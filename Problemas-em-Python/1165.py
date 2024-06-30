qtd = int(input())

for x in range(1, qtd+1):
    num = int(input())

    c = 0
    for y in range(1, num+1):
        if num % y == 0:
            c += 1
    
    if c == 2:
        print(f'{num} eh primo')
    else:
        print(f"{num} nao eh primo")
