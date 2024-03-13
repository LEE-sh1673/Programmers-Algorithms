from sys import stdin
from itertools import product

input = stdin.readline


def solution(n, m):
    numbers = [str(i) for i in range(1, n + 1)]
    numbers = map(lambda nums: " ".join(nums), product(numbers, repeat=m))
    print("\n".join(numbers))


n, m = map(int, input().split())
solution(n, m)
