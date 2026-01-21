from math import sqrt

vx = input().split()
vy = input().split()
x1, y1 = vx
x2, y2 = vy
d = sqrt((pow(float(x2) - float(x1), 2)) + (pow(float(y2) - float(y1), 2)))
print('%.4f' % d)
