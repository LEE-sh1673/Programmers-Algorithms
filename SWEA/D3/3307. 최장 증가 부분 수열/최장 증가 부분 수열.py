#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())


def sol(n, nums):
    dp = [1] * n
    for i in range(1, n):
        length = 0
        for j in range(0, i): # n-2
            if nums[j] < nums[i]:
            	dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    print(f'#{test_case} {sol(n, nums)}')
