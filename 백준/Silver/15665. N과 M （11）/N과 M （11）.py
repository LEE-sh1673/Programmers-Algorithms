"""
15665. n과 m
"""


def dfs(current):
    if len(current) == m:
        curr = ' '.join(map(str, current))

        if curr not in visited:
            visited.add(curr)
            print(curr)
        return
    else:
        for i in range(n):
            current.append(numbers[i])
            dfs(current)
            current.pop()


n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = set()
dfs([])
