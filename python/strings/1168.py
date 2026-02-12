qtd = int(input())

for i in range(qtd):
    soma = 0
    value = input()

    for x in value:
        if x == '0':
            soma += 6
        elif x == '1':
            soma += 2
        elif x == '2':
            soma += 5
        elif x == '3':
            soma += 5
        elif x == '4':
            soma += 4
        elif x == '5':
            soma += 5
        elif x == '6':
            soma += 6
        elif x == '7':
            soma += 3
        elif x == '8':
            soma += 7
        elif x == '9':
            soma += 6

    print(f"{soma} leds")
