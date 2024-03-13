"""
15652. N과 M (4)
"""
from sys import stdin

input = stdin.readline


def solution(n, m):
    def dfs(numbers):
        if len(numbers) == m:
            print(" ".join(map(str, numbers)))
            return

        for number in range(1, n + 1):
            if numbers and numbers[-1] > number:
                continue

            numbers.append(number)
            dfs(numbers)
            numbers.pop()

    dfs([])


n, m = map(int, input().split())
solution(n, m)
