from sys import stdin
from bisect import bisect_left

input = stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
check = []

for i in range(n):
    if not check or check[-1] < numbers[i]:
        check.append(numbers[i])
    else:
        check[bisect_left(check, numbers[i])] = numbers[i]

print(len(check))
