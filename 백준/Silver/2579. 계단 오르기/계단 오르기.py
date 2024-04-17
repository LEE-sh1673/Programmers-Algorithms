from sys import stdin

n = int(stdin.readline())


def solution(n):
    nums = []
    for _ in range(n):
        nums.append(int(stdin.readline()))

    if n == 1:
        return nums[0]

    if n == 2:
        return sum(nums)

    nums = [0] + nums
    dp = [0] * (n + 1)
    dp[1] = nums[1]
    dp[2] = nums[1] + nums[2]

    for h in range(3, n+1):
        dp[h] = max(nums[h] + dp[h-2], dp[h-3] + nums[h-1] + nums[h])
    return dp[-1]

print(solution(n))
