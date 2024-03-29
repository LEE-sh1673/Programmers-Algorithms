from sys import stdin

n = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().strip().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[j] > nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))