def fibonacci(n):
    if n == 1:
        return '0'
    elif n == 2:
        return '0 1'
    else:
        a = 0
        b = 1
        resultado = ['0', '1']
        for x in range(n - 2):
            c = a + b
            resultado.append(str(c))
            a = b
            b = c
        return ' '.join(resultado)

N = int(input())
print(fibonacci(N))
