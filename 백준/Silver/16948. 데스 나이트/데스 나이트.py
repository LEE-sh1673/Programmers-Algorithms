"""
1948. 데스 나이트
"""
from sys import stdin, maxsize
from collections import deque

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

input = stdin.readline
n = int(input())
r1, c1, r2, c2 = map(int, input().split())

visited = [[False] * n for _ in range(n)]
visited[r1][c1] = True

que = deque()
que.append((r1, c1, 0))
answer = maxsize

while que:
    x, y, cnt = que.popleft()

    if x == r2 and y == c2:
        answer = min(answer, cnt)
        continue

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if not visited[nx][ny]:
            visited[nx][ny] = True
            que.append((nx, ny, cnt + 1))

print(-1 if answer == maxsize else answer)
