i = 1
i2 = 3
s = 1

while (i2 <= 39):
    s += i2 / (i*2)
    i = i*2
    i2 += 2
    
print(f"{s:.2f}")
