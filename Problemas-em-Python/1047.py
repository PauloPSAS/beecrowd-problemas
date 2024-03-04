def entrada():
    return map(int, input().split())


def horas_de_jogo(hi, mi, hf, mf):
    minutos = (60 - mi + mf) % 60
    horas = (24 + hf - hi - (mi > mf)) % 24

    if horas == 0 and minutos == 0:
        horas = 24

    return horas, minutos


hI, mI, hF, mF = map(int, input().split())
houras = 24 + hF
hours, minutes = horas_de_jogo(hI, mI, hF, mF)
print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")
