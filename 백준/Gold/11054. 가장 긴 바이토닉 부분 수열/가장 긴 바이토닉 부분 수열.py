from sys import stdin


def solution(n):
    nums = list(map(int, input().split()))
    dp = [1] * n
    r_dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if nums[j] < nums[i]:
                r_dp[i] = max(r_dp[i], r_dp[j] + 1)

    answer = 0
    for i in range(n):
        answer = max(answer, dp[i] + r_dp[i] - 1)
    return answer


input = stdin.readline
n = int(input())
print(solution(n))
