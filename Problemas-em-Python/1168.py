qtd = int(input())

leds = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)

for i in range(qtd):
    soma = 0
    value = int(input())

    valueD = str(value)
    for x in valueD:
        soma += leds[int(x)]
        
    print(f"{soma} leds")
