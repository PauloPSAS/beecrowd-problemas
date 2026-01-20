qtdCompetidores, qtdFolhas, qtdFolhasCompedidores = map(int, input().split())
total =  qtdFolhas / qtdCompetidores

if total < qtdFolhasCompedidores:
    print("N")
else:
    print("S")
