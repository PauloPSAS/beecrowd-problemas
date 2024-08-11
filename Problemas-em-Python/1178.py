value = float(input())
N = [0] * 100

N[0] = value

for i in range(1, 100):
    N[i] = N[i -1] / 2.0

for i in range(100):
    print("N[{}] = {:.4f}".format(i, N[i]))
