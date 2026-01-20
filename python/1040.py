n1, n2, n3, n4 = map(float, input().split())

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / (2 + 3 + 4 + 1)

if media >= 7.:
    print("Media: {:.1f}".format(media))
    print("Aluno aprovado.")
elif media < 5.:
    print("Media: {:.1f}".format(media))
    print("Aluno reprovado.")
else:
    print("Media: {:.1f}".format(media))
    print("Aluno em exame.")
    nx = float(input())
    print(f"Nota do exame: {nx:.1f}")
    media = (media + nx) / 2
    if media >= 5.:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media))
