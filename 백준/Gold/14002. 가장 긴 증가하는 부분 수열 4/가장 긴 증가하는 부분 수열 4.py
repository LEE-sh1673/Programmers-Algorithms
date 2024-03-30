from sys import stdin
from bisect import bisect_left

input = stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# check = []
# for i in range(n):
#     if not check or check[-1] < numbers[i]:
#         check.append(numbers[i])
#     else:
#         check[bisect_left(check, numbers[i])] = numbers[i]
#     dp[i] = len(check)

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
