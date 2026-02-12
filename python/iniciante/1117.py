def invalido():
    return print("nota invalida")


def media(v1, v2):
    return  float((v1 + v2) / 2)

while True:
    n1 = float(input())
    if n1 < 0 or n1 > 10.:
        invalido()
    else:
        break

while True:
    n2 = float(input())
    if n2 < 0  or n2 > 10.:
        invalido()
    else:
        break

print(f"media = {media(n1, n2):.2f}")
