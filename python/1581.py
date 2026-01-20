n = int(input())

for _ in range(n):
    k = int(input())

    idioma = input()
    msmIdioma = True
    for i in range(1, k):
        s = input()

        if s != idioma:
            msmIdioma = False
    
    print("ingles" if not msmIdioma else idioma)
    