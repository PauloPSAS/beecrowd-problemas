media = int(input())
nota = ''

if media == 0:
    nota = 'E'
elif 0 < media <= 35:
    nota = 'D'
elif 36 <= media <= 60:
    nota = 'C'
elif 61 <= media <= 85:
    nota = 'B'
else:
    nota = 'A'
print(nota)
