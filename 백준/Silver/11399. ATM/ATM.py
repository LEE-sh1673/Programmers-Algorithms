from sys import stdin

input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(sum([sum(nums[:i+1]) for i in range(len(nums))]))
