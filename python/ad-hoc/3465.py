def converte(x, y, z):
	lista = [x, y, z]
	listaInt = list(map(int, lista))
	return listaInt[0], listaInt[1], listaInt[2]


a, b, c = input().split()
a, b, c  = converte(a, b, c)

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"{area:.3f} m2")
