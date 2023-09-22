"""Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo,
sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.
    Entrada
        A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
    Saída
        Apresente a duração do jogo conforme exemplo do beecrowd."""


def entrada():
    comeca, termina = input().split()
    return int(comeca), int(termina)


def horas_de_jogo(i, f):
    if i >= f:
        t = 24 - i
        t += f
    else:
        t = f - i
    return t


inicio, fim = entrada()
horasDeJogo = horas_de_jogo(inicio, fim)

print(f"O JOGO DUROU {horasDeJogo} HORA(S)")
