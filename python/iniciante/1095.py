i = list()
j = list()
for num in range(1, 40, 3):
    i.append(num)

for num in range(60, -1, -5):
    j.append(num)

for v in range(0, 13):
    print(f"I={i[v]} J={j[v]}")
