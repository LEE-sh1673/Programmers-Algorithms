"""
4179. 불
"""
from collections import deque

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

f_dist = [[0] * C for _ in range(R)]
j_dist = [[0] * C for _ in range(R)]

fires = deque()
js = deque()

for i in range(R):
    for j in range(C):
        f_dist[i][j] = -1
        j_dist[i][j] = -1

        if board[i][j] == 'F':
            f_dist[i][j] = 0
            fires.append((i, j))

        elif board[i][j] == 'J':
            j_dist[i][j] = 0
            js.append((i, j))

while fires:
    x, y = fires.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 > nx or 0 > ny or nx >= R or ny >= C:
            continue

        if board[nx][ny] == '#' or f_dist[nx][ny] >= 0:
            continue

        f_dist[nx][ny] = f_dist[x][y] + 1
        fires.append((nx, ny))

"""
-1 -1 -1 -1 
-1 1 0 -1 
-1 2 1 -1 
-1 3 2 -1
"""
answer = -1
is_exit = False

while js and not is_exit:
    x, y = js.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 > nx or 0 > ny or nx >= R or ny >= C:
            answer = j_dist[x][y] + 1
            is_exit = True
            break

        if board[nx][ny] == '#' or j_dist[nx][ny] >= 0:
            continue

        if 0 <= f_dist[nx][ny] <= j_dist[x][y] + 1:
            continue

        j_dist[nx][ny] = j_dist[x][y] + 1
        js.append((nx, ny))

print('IMPOSSIBLE' if not is_exit else answer)
