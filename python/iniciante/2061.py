abas, acoes = map(int, input().split())

for _ in range(acoes):
    acao = input().lower().strip()

    if acao == 'fechou':
        abas += 1
    elif acao == 'clicou':
        abas -= 1
    
print(abas)