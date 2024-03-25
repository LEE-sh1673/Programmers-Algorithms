from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
target = int(stdin.readline())
print(nums.count(target))
