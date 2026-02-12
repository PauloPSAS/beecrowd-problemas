def converte_auto(t1, t2):
    dif = t2 - t1

    days = dif // (24 * 60 * 60)
    dif %= (24 * 60 * 60)

    hours = dif // (60 * 60)
    dif %= (60 * 60)

    minutes = dif // 60
    dif %= 60

    seconds = dif

    return days, hours, minutes, seconds


def main():
    day1 = int(input().split()[1])
    h1, m1, s1 = map(int, input().split(":"))
    temp1 = s1 + (m1 * 60) + (h1 * 60 * 60) + (day1 * 24 * 60 * 60)


    day2 = int(input().split()[1])
    h2, m2, s2 = map(int, input().split(":"))
    temp2 = s2 + (m2 * 60) + (h2 * 60 * 60) + (day2 * 24 * 60 * 60)

    d, h, m, s = converte_auto(temp1, temp2)

    print(f"{d} dia(s)")
    print(f"{h} hora(s)")
    print(f"{m} minuto(s)")
    print(f"{s} segundo(s)")


if __name__ == '__main__':
    main()
    