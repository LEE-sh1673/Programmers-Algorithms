for _ in range(int(input())):
    n = int(input())
    dp = [[1, 0], [0, 1]] + [[0, 0] for _ in range(n - 1)]

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 2][0] + dp[i - 1][0]
        dp[i][1] = dp[i - 2][1] + dp[i - 1][1]

    print(*dp[n])
