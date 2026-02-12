while True:
    valorInvalido = False
    a = float(input())
    if a > 10. or a < 0:
        while True:
            print("nota invalida")
            a = float(input())
            if 0 < a <= 10.:
                break

    b = float(input())
    if b > 10. or b < 0:
        while True:
            print("nota invalida")
            b = float(input())
            if 0 < b <= 10.:
                break

    print(f"media = {(a+b)/2:.2f}")
    print("novo calculo (1-sim 2-nao)")
    novoCalculo = int(input())

    while True:
        if novoCalculo == 1 or novoCalculo == 2:
            break
        else:
            print("novo calculo (1-sim 2-nao)")
            novoCalculo = int(input())

    if novoCalculo == 2:
        break
