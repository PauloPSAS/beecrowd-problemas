lista = []
a, b = map(int, input().split())
c = 0
conteb = 1


lista[input()]


altp, altm, altg =  map(int, input().split())

for x in lista:
    if x == 'P':
        c += altp
        if c > b:
            conteb += 1
            b += b

    
    elif x == 'M':
        c += altm
        if c > b:
            conteb += 1
            b += b

    elif x == 'G':
        c += altg
        if c > b:
            conteb += 1
            b += b

print(conteb)
