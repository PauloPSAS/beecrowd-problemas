import sys

# Finaliza com EOF (Não se sabe previamente quantas linhas ou quantos casos
# de teste vão ser fornecidos)
for linha in sys.stdin:

    # Atribui False a itático e a negrito para determinar
    # Se é a tag de abertura ou de fechamento
    italico = negrito = False
    
    novoTxt = ""

    for caractere in linha:

        # Se o caractere for underline:
        if caractere == "_":

            # Verifica se é a ultima tag foi de abertura ou fechamento
            # Caso a anterior foi abertura irá cair aqui e fechar a tag
            if italico == True:
                novoTxt += "</i>"
            
            # Caso italico for False , logo será a tag de abertura
            else:
                novoTxt += "<i>"
            
            # Altera o valor booleano indicando que mudou a abertura/fechamento da tag
            italico = not italico
        
        # Se o caractere for Estrelinha
        elif caractere == "*":

            # Verifica se negrito é verdadeiro.
            # Caso seja indica que é tag de fechamento
            if negrito == True:
                novoTxt += "</b>"
            
            # Se negrito é Falso, indica que é tag de abertura
            else:
                novoTxt += "<b>"
            
            # Altera o valor booleano indicando que mudou a abertura/fechamento da tag
            negrito = not negrito
        
        # Se não for nenhuma das tags apenas adiciona o caractere no novo texto
        else:
            novoTxt += caractere

    print(novoTxt, end="")
