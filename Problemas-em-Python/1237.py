# Estranhamente no meu da erro de time mas no de alguns colegas não dá
def maiorSubstring(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0

    for i in range(n):
        for j in range(m):
            if s1[i] == s2[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                max_len = max(max_len, dp[i + 1][j + 1])
    
    return max_len


while True:
    try:
        string1 = input()
        string2 = input()

        print(maiorSubstring(string1, string2))

    except EOFError:
        break