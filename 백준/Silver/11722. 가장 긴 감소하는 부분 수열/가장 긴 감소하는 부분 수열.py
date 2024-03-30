from sys import stdin

input = stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n
check = []


def lower_bound(target):
    start, end = 0, len(check) - 1

    while start < end:
        mid = start + (end - start) // 2

        if check[mid] <= target:
            end = mid
        else:
            start = mid+1
    return start


for i in range(n):
    if not check or check[-1] > nums[i]:
        check.append(nums[i])
    else:
        check[lower_bound(nums[i])] = nums[i]
    dp[i] = len(check)

print(max(dp))