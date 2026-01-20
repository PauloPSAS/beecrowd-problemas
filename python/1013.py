num = input().split()
a, b, c = num
maiorAB = (int(a) + int(b) + (abs(int(a) - int(b)))) / 2
maiorABC = (int(maiorAB) + int(c) + (abs(int(maiorAB) - int(c)))) / 2
print('{} eh o maior'.format(int(maiorABC)))