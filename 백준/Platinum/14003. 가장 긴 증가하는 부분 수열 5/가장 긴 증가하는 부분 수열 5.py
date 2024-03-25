from sys import stdin

n = int(stdin.readline().strip())
nums = list(map(int, stdin.readline().strip().split()))
dp = [1] * n
check = []


def bin_search(target):
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
        dp[i] = len(check)
    else:
        idx = bin_search(nums[i])
        check[idx] = nums[i]
        dp[i] = idx + 1

target = max(dp)
lis = []

for i in range(n-1, -1, -1):
    if target < 1:
        break
        
    if dp[i] == target:
        lis.append(nums[i])
        target -= 1

print(max(dp))
print(*lis[::-1])
