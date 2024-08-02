i =  cDecimal = 0

while i < 2:
    if i == 0:
        j = 1
    elif i == 1:
        j = 2
    else:
        j = 3
    for x in range(1, 4):
        print(f"I={i:.0f} J={j:.0f}" if cDecimal == 0 else f"I={i:.0f}.{cDecimal} J={j:.0f}.{cDecimal}")
        j += 1
    cDecimal += 2
    if cDecimal > 8:
        i += 1
        cDecimal = 0
i = 2
j = 3
for x in range(3):
    print(f'I={i} J={j}')
    j += 1