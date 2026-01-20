# Crescimento populacional

casosDeTeste = int(input())

for _ in range(casosDeTeste):
    pa, pb, g1, g2 = input().split()
    
    pa, pb = int(pa), int(pb)
    g1, g2 = float(g1), float(g2)

    anos = 0    
    
    while pa <= pb:

        pa = int(pa + (pa * g1 / 100))
        pb = int(pb + (pb * g2 / 100))
        anos += 1


        if anos > 100:
    
            break
    
    print("Mais de 1 seculo." if anos > 100 else f"{anos} anos.")
