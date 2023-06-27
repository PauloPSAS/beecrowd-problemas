# Tipos de triângulos.
def ordem(l):
    # Vai criar uma lista em ordem decrescente dos lados
    lOrdenados = sorted(l, reverse=True)
    return lOrdenados


def lados():
    # Vai da o input dos três lados do triângulo
    l1, l2, l3 = input().split()
    la = [float(l1), float(l2), float(l3)]
    return la


def tipo_de_triangulo(lo):
    # vai mostrar o tipo de triângulo criado
    if lo[0] >= lo[1] + lo[2]:
        print("NAO FORMA TRIANGULO")
    elif lo[0] ** 2 == (lo[1] ** 2) + lo[2] ** 2:
        print("TRIANGULO RETANGULO")
    elif lo[0] ** 2 > (lo[1] ** 2) + (lo[2] ** 2):
        print("TRIANGULO OBTUSANGULO")
    elif lo[0] ** 2 < (lo[1] ** 2) + (lo[2] ** 2):
        print("TRIANGULO ACUTANGULO")

    if lo[0] == lo[1] == lo[2]:
        print("TRIANGULO EQUILATERO")
    elif lo[0] == lo[1] or lo[0] == lo[2] or lo[1] == lo[2]:
        print("TRIANGULO ISOSCELES")


la = lados()
ladosOrdenados = ordem(la)
tipo_de_triangulo(ladosOrdenados)
