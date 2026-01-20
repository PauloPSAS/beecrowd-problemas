inicio, final = map(int, input().split())

if inicio >= final:
    horasJogo = 24 - inicio
    horasJogo += final
else:
    horasJogo = final - inicio
print(f"O JOGO DUROU {horasJogo} HORA(S)")
