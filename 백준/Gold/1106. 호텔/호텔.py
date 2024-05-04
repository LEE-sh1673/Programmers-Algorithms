from sys import maxsize

C, N = map(int, input().split())
costs = [tuple(map(int, input().split())) for _ in range(N)]
dp = [maxsize] * 1101
dp[0] = 0

for cost, cnt in costs:
    for i in range(cnt, 1101):
        dp[i] = min(dp[i-cnt] + cost, dp[i])

print(min(dp[C:]))
