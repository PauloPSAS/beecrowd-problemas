def formula(v):
    if 0 <= v <= 25.00:
        print('Intervalo [0,25]')
    elif 25. <= v <= 50.00:
        print('Intervalo (25,50]')
    elif 50. <= v <= 75.00:
        print('Intervalo (50,75]')
    elif 75. <= v <= 100.00:
        print('Intervalo (75,100]')
    else:
        print('Fora de intervalo')


valor = float(input())
formula(valor)
