# O código está certo porém está dando erro 'Time limit exceeded' e não consegui resolver ainda

def main():
    n = 1
    qtt = int(input())

    while qtt > 0:
        ConsumoFinal, total_pessoas = 0, 0
        listaPessoa = {}

        for _ in range(qtt):
            A, B = map(int, input().split())
            consumo = B // A
            listaPessoa[consumo] = listaPessoa.get(consumo, 0) + A
            ConsumoFinal += B
            total_pessoas += A

        if n > 1:
            print()

        print(f"Cidade# {n}:")
        print(' '.join(f"{listaPessoa[p]}-{p}" for p in sorted(listaPessoa.keys())))
        
        consumo_medio = ConsumoFinal / total_pessoas
        resultado = f"{consumo_medio:.3f}"
        resultado = resultado[:resultado.index('.') + 3]
        print(f"Consumo medio: {resultado} m3.")
        
        n += 1
        qtt = int(input())

if __name__ == "__main__":
    main()
