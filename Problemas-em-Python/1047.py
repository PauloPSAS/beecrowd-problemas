"""Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
Observação: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
    Entrada
        Quatro números inteiros representando a hora de início e fim do jogo.
    Saída
        Mostre a seguinte mensagem: 'O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)'."""


def entrada():
    return map(int, input().split())


def horas_de_jogo(hi, mi, hf, mf):
    minutos = (60 - mi + mf) % 60
    horas = (24 + hf - hi - (mi > mf)) % 24

    if horas == 0 and minutos == 0:
        horas = 24

    return horas, minutos


hI, mI, hF, mF = entrada()
hours, minutes = horas_de_jogo(hI, mI, hF, mF)
print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")
