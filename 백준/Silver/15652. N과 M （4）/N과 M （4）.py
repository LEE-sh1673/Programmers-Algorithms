"""
15652. N과 M (4)
"""
from sys import stdin

input = stdin.readline


def solution(n, m):
    from itertools import combinations_with_replacement
    numbers = [str(i) for i in range(1, n + 1)]
    numbers = map(lambda nums: " ".join(nums), combinations_with_replacement(numbers, m))
    print("\n".join(numbers))


n, m = map(int, input().split())
solution(n, m)
