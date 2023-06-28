"""Reajuste de salário de acordo com a tabela:
        Salário	                    Percentual de Reajuste
        0 - 400.00                      15%
        400.01 - 800.00                 12%
        800.01 - 1200.00                10%
        1200.01 - 2000.00               7%
        Acima de 2000.00                4%"""


def saida(sf, a, p):
    print(f"Novo salario: {sf:.2f}")
    print(f"Reajuste ganho: {a:.2f}")
    print(f"Em percentual: {p} %")


def reajuste_salarial(s):
    if s > 2000.00:
        prc = 4
    elif s > 1200.00:
        prc = 7
    elif s > 800.00:
        prc = 10
    elif s > 400.00:
        prc = 12
    else:
        prc = 15

    aumento = s / 100 * prc
    salarioF = s + aumento

    saida(salarioF, aumento, prc)


salario = float(input())
reajuste_salarial(salario)
