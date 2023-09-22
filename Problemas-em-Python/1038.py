valores = input().split()

c, q = valores
total = 0

c = int(c)
q = float(q)

if c == 1:
    total = 4 * q

elif c == 2:
    total = 4.50 * q

elif c == 3:
    total = 5 * q

elif c == 4:
    total = 2 * q

elif c == 5:
    total = 1.50 * q

print(f'Total: R$ {total:.2f}')
