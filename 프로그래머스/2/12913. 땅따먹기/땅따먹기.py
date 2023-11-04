# def solution(land):
#     answer = 0

#     def dfs(H, M, count):
#         nonlocal answer
        
#         if H + 1 == len(land):
#             answer = max(answer, count)    
#         else:
#             for i in range(4):
#                 if i == M:
#                     continue
                    
#                 dfs(H+1, i, count + land[H+1][i])
    
#     for i in range(4):
#         dfs(0, i, land[0][i])
        
#     return answer


def solution(land):
    n = len(land)
    dp = [[0] * 4 for _ in range(n)]
    
    for i in range(4):
        dp[0][i] = land[0][i]
    
    for i in range(1, n):
        dp[i][0] = land[i][0] + max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
        dp[i][1] = land[i][1] + max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
        dp[i][2] = land[i][2] + max(dp[i-1][0], dp[i-1][1], dp[i-1][3])
        dp[i][3] = land[i][3] + max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        
    return max(dp[n-1])
    