from sys import stdin

input = stdin.readline


def solution(n, m):
    visited = []

    def dfs(start):
        if len(visited) == m:
            print(' '.join(map(str, visited)))
            return

        for i in range(start, n+1):
            if i not in visited:
                visited.append(i)
                dfs(i+1)
                visited.pop()
    dfs(1)


n, m = map(int, input().split())
solution(n, m)
