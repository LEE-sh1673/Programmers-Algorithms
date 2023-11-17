"""
DP[N] = 가로의 길이가 N일 때 타일을 채우는 방법의 수

DP[1] = 1
DP[2] = 2
DP[3] = 2 * DP[1] + 1 = 3
DP[4] = 2 * DP[2] + 1 = 5
DP[5] = 2 * DP[3] + 1 = 7

"""
def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1_000_000_007
    
    return dp[n]

