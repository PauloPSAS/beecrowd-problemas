num = int(input())
seq = 1
vop = 0

for x in range(num):
    v = int(input())
    if vop == 0 or vop == v:
        vop = v
    else:
        seq += 1
        vop = v
print(seq)
