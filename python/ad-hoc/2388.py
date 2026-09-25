intervalos_registrados = int(input())
distancia_percorrida = 0

for _ in range(intervalos_registrados):
    tempo_decorrido, velocidade_media = map(int, input().split())
    distancia_percorrida += (tempo_decorrido * velocidade_media)

print(distancia_percorrida)