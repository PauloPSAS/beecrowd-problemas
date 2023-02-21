r = list(map(float, input().split()))

if r[0] < r[1] + r[2] and r[1] < r[0] + r[2] and r[2] < r[0] + r[1]:
    print("Perimetro = {:.1f}".format(r[0]+r[1]+r[2]))
else:
    print("Area = {:.1f}".format(((r[0]+r[1])*r[2])/2))
