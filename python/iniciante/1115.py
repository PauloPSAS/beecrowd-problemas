result = list()
while True:
	x, y = map(int, input().split())
	if x > 0 and y > 0:
		result.append("primeiro")
	elif x < 0 and y > 0:
		result.append("segundo")
	elif x < 0 and y < 0:
		result.append("terceiro")
	elif x > 0 and y < 0:
		result.append("quarto")
	else:
		break

for z in range(0, len(result)):
	print(result[z])
