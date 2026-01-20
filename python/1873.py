qtd = int(input())

for v in range(qtd):
    raj, shelly = input().split()
    if raj == shelly:
        print("empate")
    elif (raj == 'pedra' and shelly == 'tesoura') or \
         (raj == 'pedra' and shelly == 'lagarto') or \
         (raj == 'papel' and shelly == 'pedra') or \
         (raj == 'papel' and shelly == 'spock') or \
         (raj == 'tesoura' and shelly == 'papel') or \
         (raj == 'tesoura' and shelly == 'lagarto') or \
         (raj == 'lagarto' and shelly == 'spock') or \
         (raj == 'lagarto' and shelly == 'papel') or \
         (raj == 'spock' and shelly == 'tesoura') or \
         (raj == 'spock' and shelly == 'pedra'):
        print("rajesh")
    else:
        print("sheldon")
