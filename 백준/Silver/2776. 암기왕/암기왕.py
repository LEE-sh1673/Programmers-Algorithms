from sys import stdin
from bisect import bisect_left


def exists(nums, target):
    return (idx := bisect_left(nums, target)) != n and nums[idx] == target


input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))
    nums.sort()
    print('\n'.join(['1' if exists(nums, target) else '0' for target in targets]))
    