grenais = vInter = vGremio = empate = 0
while True:
    inter, gremio = map(int, input().split())
    grenais += 1

    if inter > gremio:
        vInter += 1
    elif gremio > inter:
        vGremio += 1
    else:
        empate += 1
    while True:
        print("Novo grenal (1-sim 2-nao)")
        pgt = int(input())
        if pgt == 1 or pgt == 2:
            break
    if pgt == 2:
        break
print(f"{grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")
if vInter > vGremio:
    print("Inter venceu mais")
elif vGremio > vInter:
    print("Gremio venceu mais")
