casos = int(input())

for i in range(casos):
    numero = int(input())

    # número for 0
    if numero == 0:
        print("NULL")
    
    # Senão, se número é par e negativo
    elif numero % 2 == 0 and numero < 0:
        print("EVEN NEGATIVE")
    
    # Se não, se número é par e positvo
    elif numero % 2 == 0 and numero > 0:
        print("EVEN POSITIVE")
    
    # Se não, se número é ímpar e negativo
    elif numero % 2 != 0 and numero < 0:
        print("ODD NEGATIVE")
    
    # Se nenhuma condição for verdadeira, cairá no else
    else:
        print("ODD POSITIVE")
