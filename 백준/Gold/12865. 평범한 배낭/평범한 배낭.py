"""
dp[N][K] = 무게가 K일때, N까지 뽑았을 때의 최대 가치

dp[N][K]를 정할 때,

if. 물건의 무게가 배낭 무게(W)를 초과할 때 (w[N] > W)
    - dp[N][K] = dp[N-1][K]
else.
    - dp[N][K] = max(dp[N-1][K], v[N] + dp[N-1][K-w[N]]))
"""
n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
weights = [0]
values = [0]

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

for i in range(1, n+1):
    for w in range(1, k+1): # 무게가 w일때, i까지 뽑은 최대 가치 
        if w < weights[i]:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], values[i] + dp[i-1][w - weights[i]])

print(dp[n][k])
