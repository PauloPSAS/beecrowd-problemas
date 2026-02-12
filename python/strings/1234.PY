import sys

# Este for considera varios casos de Teste EOF
# Como não está especificado na descrição da questão
# para não usar 'while True' optei por esse método
for frase in sys.stdin:

    maiusculo = False
    novoTxt = ""

    # posicao representa o indice da letra e letra é autoexplicativo.
    # o enumerate(frase) irá percorrer cada letra separando sua letra e o
    # indice ao qual a letra pertence.
    for posicao, letra in enumerate(frase):
        
        # Se é a primeira letra da frase e é uma letra OU se é letra e a ultima é minuscula.
        #Se qualquer uma dessas condições entre o OU é verdadeira, executa o if.
        if (posicao == 0 and letra.isalpha()) or (letra.isalpha() and maiusculo == False):
            novoTxt += letra.upper()
            maiusculo = not maiusculo
        
        # Se não, se é uma letra e ela a ultima foi maiuscula
        elif letra.isalpha() and maiusculo == True:
            novoTxt += letra.lower()
            maiusculo = not maiusculo
        
        # Se não, não será letra
        else:
            novoTxt += letra
    
    print(novoTxt, end="")
