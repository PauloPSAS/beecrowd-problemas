gasolina = 0
diesel = 0
alcool = 0
while True:
    value = int(input())
    if value <= 3 and value >= 1:
        if value == 1:
            alcool += 1
        elif value == 2:
            gasolina += 1
        else:
            diesel += 1

    elif value == 4:
        print("MUITO OBRIGADO")
        print("Alcool: %d" % alcool)
        print("Gasolina: %d" % gasolina)
        print("Diesel: %d" % diesel)
        break
