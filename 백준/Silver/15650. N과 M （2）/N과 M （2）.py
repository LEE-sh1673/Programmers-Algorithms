from sys import stdin

input = stdin.readline


def dfs(n, m, curr):
    if len(curr) == m:
        print(*curr)
    else:
        for i in range(1, n + 1):
            if visited[i - 1] or (curr and curr[-1] >= i):
                continue

            visited[i - 1] = True
            curr.append(i)
            dfs(n, m, curr)
            visited[i - 1] = False
            curr.remove(i)


n, m = map(int, input().split())
visited = [False] * n
dfs(n, m, [])