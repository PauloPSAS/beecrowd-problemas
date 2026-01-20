par = []
impar = []

for i in range(15):
    num = int(input())
    
    if num % 2 == 0:
        par.append(num)
        if len(par) == 5:
            for j in range(5):
                print(f"par[{j}] = {par[j]}")
            par.clear()
    else:
        impar.append(num)
        if len(impar) == 5:
            for j in range(5):
                print(f"impar[{j}] = {impar[j]}")
            impar.clear()

for j in range(len(impar)):
    print(f"impar[{j}] = {impar[j]}")

for j in range(len(par)):
    print(f"par[{j}] = {par[j]}")
