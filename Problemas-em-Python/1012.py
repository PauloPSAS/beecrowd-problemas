lista = input().split(' ')
a, b, c = lista
triangulo = float(a) * float(c) / 2
circulo = 3.14159 * float(c) ** 2
trapezio = (float(a) + float(b)) * float(c) / 2
quadrado = float(b) ** 2
retangulo = float(a) * float(b)
print('TRIANGULO: %0.3f' % triangulo)
print('CIRCULO: %.03f' % circulo)
print('TRAPEZIO: %0.3f' % trapezio)
print('QUADRADO: %0.3f' % quadrado)
print('RETANGULO: %0.3f' % retangulo)
