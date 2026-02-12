linha1 = input().split(" ")
linha2 = input().split(" ")

cod1, qdt1, valor1 = linha1
cod2, qdt2, valor2 = linha2

total = (int(qdt1) * float(valor1) + int(qdt2) * float(valor2))
print('VALOR A PAGAR: R$ %0.2f' % total)
