from sys import stdin
from bisect import bisect_left


def solution(n):
    def max_increase_sequence(numbers):
        check = []
        dp = [1] * n

        for i in range(n):
            if not check or check[-1] < numbers[i]:
                check.append(numbers[i])
            else:
                check[bisect_left(check, numbers[i])] = numbers[i]
            dp[i] = len(check)
        return dp

    nums = list(map(int, input().split()))
    dp = max_increase_sequence(nums)
    r_dp = max_increase_sequence(nums[::-1])[::-1]
    return max([a + b - 1 for a, b in zip(dp, r_dp)])


input = stdin.readline
n = int(input())
print(solution(n))
