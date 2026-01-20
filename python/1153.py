n = int(input())
f = n
t = 1
for f in range(n, 0, -1):
    t *= f
print(t)
