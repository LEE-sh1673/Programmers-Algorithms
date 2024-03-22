"""
15655. N과 M (8)
"""
from sys import stdin

input = stdin.readline


def solution(m):
    from itertools import combinations_with_replacement
    numbers = [int(num) for num in input().split()]
    numbers = combinations_with_replacement(map(str, sorted(numbers)), m)
    print('\n'.join(list(map(' '.join, numbers))))


n, m = map(int, input().split())
solution(m)
