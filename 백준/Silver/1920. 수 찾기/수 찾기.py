from sys import stdin
from bisect import bisect_left


def exists(nums, target):
    return (idx := bisect_left(A, target)) != len(nums) and A[idx] == target


N = int(stdin.readline())
A = sorted(list(map(int, stdin.readline().split())))
M = int(stdin.readline())
B = list(map(int, stdin.readline().split()))
print('\n'.join(['1' if exists(A, num) else '0' for num in B]))