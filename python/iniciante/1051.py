a = float(input())

if 0 < a <= 2000:
    print("Isento")

elif 2000 < a <= 3000:
    t = a - 2000
    tx = t * 8 / 100
    print(f"R$ {tx:.2f}")

elif 3000 < a <= 4500:
    t = a - 2000
    t1 = t - 1000
    tx1 = 1000 * 8 / 100
    tx2 = t1 * 18 / 100
    print(f"R$ {tx1+tx2:.2f}")

else:
    t = a - 2000
    t1 = t - 1000
    tx1 = 1000 * 8 / 100
    t2 = t1 - 1500
    tx2 =  1500 * 18 / 100
    tx = t2 * 28 / 100
    print(f"R$ {tx+tx1+tx2:.2f}")
