from sys import stdin
from bisect import bisect_left

input = stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * n
check = []

for i in range(n):
    if not check or check[-1] < numbers[i]:
        check.append(numbers[i])
        dp[i] = len(check)
    else:
        idx = bisect_left(check, numbers[i])
        check[idx] = numbers[i]
        dp[i] = idx + 1

x = max(dp)
print(x)

result = []
for i in range(n - 1, -1, -1):
    if dp[i] == x:
        result.append(numbers[i])
        x -= 1

result.reverse()
for r in result:
    print(r, end=' ')
