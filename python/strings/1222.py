import sys

for linha in sys.stdin:
    linha = linha.strip()
    if not linha:
        continue
    
    try:
        n, l, c = map(int, linha.split())
        palavras = sys.stdin.readline().strip().split()

        linhas_usadas = 1
        tamanho_linha = 0

        for palavra in palavras:
            tamanho_palavra = len(palavra)

            if tamanho_linha == 0:
                tamanho_linha = tamanho_palavra

            elif tamanho_linha + 1 + tamanho_palavra <= c:
                tamanho_linha += 1 + tamanho_palavra
            
            else:
                linhas_usadas += 1
                tamanho_linha = tamanho_palavra

        paginas = (linhas_usadas + l - 1) // l 
        print(paginas)

    except Exception as e:
        break
