valores = input().split(" ")
n1, n2, n3, n4 = valores
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((2 * n1) + (3 * n2) + (4 * n3) + (1 * n4)) / (2 + 3 + 4 + 1)

if media >= 7.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno aprovado.')
elif media < 5.0:
    print('Media: {:.1f}'.format(media))
    print('Aluno reprovado.')
else:
    exame = float(input())
    print('Media: {:.1f}'.format(media))
    print('Aluno em exame.')
    print('Nota do exame: {:.1f}'.format(exame))
    nota_final = (media + exame) / 2
    if nota_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(nota_final))
