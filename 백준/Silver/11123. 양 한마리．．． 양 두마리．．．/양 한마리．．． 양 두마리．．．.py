"""
11123. 양 한마리... 양 두마리...
"""
from collections import deque

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)


def check(i, j):
    que = deque()
    que.append((i, j))
    visited[i][j] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if not visited[nx][ny] and board[nx][ny] == '#':
                visited[nx][ny] = True
                que.append((nx, ny))


for _ in range(int(input())):
    n, m = map(int, input().split())
    board = []
    sheep = []

    for i in range(n):
        board.append([])

        for j, el in enumerate(input()):
            if el == '#':
                sheep.append((i, j))
            board[i].append(el)

    visited = [[False] * m for _ in range(n)]
    group_count = 0

    for i, j in sheep:
        if not visited[i][j]:
            check(i, j)
            group_count += 1

    print(group_count)
