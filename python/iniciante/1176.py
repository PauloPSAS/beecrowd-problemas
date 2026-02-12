def fibbonaci(n):
    li = [0, 1]

    for _ in range(2, n+1):
        li.append(li[-1] + li[-2])
    return li[n]


repetições = int(input())

for _ in range(repetições):
    n = int(input())

    resultado = fibbonaci(n)
    print("Fib({}) = {}".format(n, resultado))
