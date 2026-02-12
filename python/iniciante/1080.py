position = maior = 0

for x in range(100):
	value = int(input())

	if x == 0:
		maior = value
		position = x+1
	else:
		if value > maior:
			maior = value
			position = x+1
print(maior)
print(position)
