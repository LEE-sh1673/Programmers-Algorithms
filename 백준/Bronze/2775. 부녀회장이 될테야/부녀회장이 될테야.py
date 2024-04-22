from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    dp = [[0 for _ in range(n)] for _ in range(k+1)]

    for i in range(n):
        dp[0][i] = i + 1

    for i in range(1, k+1):
        for j in range(n):
            dp[i][j] = sum(dp[i-1][0:j+1])

    print(dp[k][n-1])

