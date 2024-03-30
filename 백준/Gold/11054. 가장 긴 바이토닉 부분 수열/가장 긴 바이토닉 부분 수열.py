from sys import stdin


def solution(n):
    nums = list(map(int, input().split()))
    check = []
    dp = [1] * n
    r_dp = [1] * n

    def lower_bound(target):
        start, end = 0, len(check) - 1

        while start < end:
            mid = start + (end - start) // 2

            if check[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start

    for i in range(n):
        if not check or check[-1] < nums[i]:
            check.append(nums[i])
        else:
            check[lower_bound(nums[i])] = nums[i]
        dp[i] = len(check)

    check = []
    for i in range(n - 1, -1, -1):
        if not check or check[-1] < nums[i]:
            check.append(nums[i])
        else:
            idx = lower_bound(nums[i])
            check[idx] = nums[i]
        r_dp[i] = len(check)

    return max([dp[i] + r_dp[i] - 1 for i in range(n)])


input = stdin.readline
n = int(input())
print(solution(n))
