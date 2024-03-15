"""
6603. 로또
"""
from itertools import combinations
from sys import stdin

input = stdin.readline

while True:
    k, *s = map(int, input().split())

    if k == 0:
        break

    numbers = [" ".join(map(str, combs)) for combs in combinations(s, 6)]
    print("\n".join(numbers), end="\n\n")
