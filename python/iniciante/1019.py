seg = int(input())

hr = seg // 60 ** 2
seg -= hr * 60 ** 2

minu = seg // 60
seg -= minu * 60

print(f'{hr}:{minu}:{seg}')
