"""
4179. 불
"""
from collections import deque

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dist = [[0] * C for _ in range(R)]
que = deque()

for i in range(R):
    for j in range(C):
        dist[i][j] = -1

        if board[i][j] == 'F':
            dist[i][j] = 0
            que.append((i, j))
        elif board[i][j] == 'J':
            J = (i, j)

while que:
    x, y = que.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 > nx or 0 > ny or nx >= R or ny >= C:
            continue

        if board[nx][ny] == '#' or dist[nx][ny] != -1:
            continue

        dist[nx][ny] = dist[x][y] + 1
        que.append((nx, ny))

x, y = J
dist[x][y] = 0
que.append((x, y))
answer = 0
is_exit = False

while que and not is_exit:
    x, y = que.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 > nx or 0 > ny or nx >= R or ny >= C:
            answer = dist[x][y] + 1
            is_exit = True
            break

        if board[nx][ny] == '#':
            continue

        if dist[nx][ny] != -1 and dist[nx][ny] <= dist[x][y] + 1:
            continue

        dist[nx][ny] = dist[x][y] + 1
        que.append((nx, ny))

print('IMPOSSIBLE' if not is_exit else answer)
