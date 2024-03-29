from sys import stdin

n = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().strip().split()))
dp = [0] * n
dp[0] = nums[0]
answer = 0

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + nums[i])
        else:
            dp[i] = max(dp[i], nums[i])

    answer = max(answer, dp[i])

print(answer)
