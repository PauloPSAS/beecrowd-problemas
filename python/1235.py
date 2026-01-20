qtdCasos = int(input())

for caso in range(qtdCasos):
    textoEmbaralhado = input()
    textoDesembaralhado = ""

    # Pega do inicio do texto embaralhado até a métade dele.
    metadeEsquerda = textoEmbaralhado[:len(textoEmbaralhado)//2]

    # Pega da metade do texto embaralhado até o final dele.
    metadeDireita = textoEmbaralhado[len(textoEmbaralhado)//2:]

    # Coloca a primeira métade do texto na nova variável de trás pra frente.
    textoDesembaralhado += metadeEsquerda[::-1]

    # Coloca a segunda métade do texto na nova variável de trás pra frente.
    textoDesembaralhado += metadeDireita[::-1]

    print(textoDesembaralhado)
