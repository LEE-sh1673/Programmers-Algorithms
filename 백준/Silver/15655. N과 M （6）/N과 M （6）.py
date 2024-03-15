"""
15655. N과 M (6)
"""
from sys import stdin

input = stdin.readline


def solution(n, m):
    visited = [False] * n
    numbers = [int(num) for num in input().split()]
    numbers.sort()

    def dfs(nums):
        if len(nums) == m:
            print(" ".join(map(str, nums)))
            return

        for i in range(n):
            if visited[i] or (nums and nums[-1] >= numbers[i]):
                continue

            visited[i] = True
            nums.append(numbers[i])
            dfs(nums)
            visited[i] = False
            nums.pop()

    dfs([])


n, m = map(int, input().split())
solution(n, m)
