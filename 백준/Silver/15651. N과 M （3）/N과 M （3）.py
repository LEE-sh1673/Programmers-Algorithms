"""
15651. N과 M (3)
"""
from sys import stdin

input = stdin.readline


def solution(n, m):
    visited = []

    def dfs():
        if len(visited) == m:
            print(*visited)
            return
        for number in range(1, n + 1):
            visited.append(number)
            dfs()
            visited.pop()
    dfs()


n, m = map(int, input().split())
solution(n, m)
