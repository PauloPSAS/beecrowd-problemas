# Tamanho do vetor
tam = int(input())

# Irá pegar os valores em uma mesma linha separado por espaço
valores = input().split()[:tam]

# Converte para int e adiciona os valores no vetor
vetor = [int(valor) for valor in valores]

# Pega o menor valor e o indice dele no vetor
menor = min(vetor)
indMenor = vetor.index(menor)

print("Menor valor: {}\nPosicao: {}".format(menor, indMenor))
