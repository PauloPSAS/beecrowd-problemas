def criptografa(txt):
    txtCp = []

    # Primeira passada: Desloca todos os caracteres alfabéticos 3 casas à direita na tabela ASCII.
    for letra in txt:
        if letra.isalpha():
            txtCp.append(chr(ord(letra) + 3))
        else:
            txtCp.append(letra)

    # Segunda passada: Inverte o texto.
    txtCpInvertido = txtCp[::-1]

    # Terceira passada: Desloca uma casa à esquerda a partir da metade do texto.
    metade = len(txtCpInvertido) // 2

    for i in range(metade, len(txtCpInvertido)):
        txtCpInvertido[i] = chr(ord(txtCpInvertido[i]) - 1)

    # Junta a lista em uma string e retorna.
    return ''.join(txtCpInvertido)


# Número de casos
n = int(input())

for _ in range(n):
    texto = str(input())
    textoCriptografado = criptografa(texto)
    print(textoCriptografado)
