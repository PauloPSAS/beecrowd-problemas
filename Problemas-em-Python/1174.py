values = []
for v in range(100):
    n = float(input())
    values.append(n)

for v in range(100):
    if values[v] <= 10.:
        print(f"A[{v}] = {values[v]:.1f}")
