# Estranhamente no meu da erro de time mas no de alguns colegas não dá
def maiorSubstring(s1, s2):
    n = len(s1)
    m = len(s2)
    
    if n < m:
        s1, s2 = s2, s1
        n, m = m, n

    prev = [0] * (m + 1)
    curr = [0] * (m + 1)
    max_len = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
                max_len = max(max_len, curr[j])
            else:
                curr[j] = 0
        prev, curr = curr, [0] * (m + 1)
    
    return max_len


while True:
    try:
        string1 = input()
        string2 = input()

        print(maiorSubstring(string1, string2))

    except EOFError:
        break