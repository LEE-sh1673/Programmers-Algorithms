"""
4179. 불

- 지훈이의 위치와 불이 붙은 위치를 감안해서
     - 지훈이가 불에 타기전에 탈출할 수 있는지의 여부
     - 그리고 얼마나 빨리 탈출할 수 있는지를

- 지훈이와 불은 매 분마다 한칸씩 수평또는 수직으로(비스듬하게 이동하지 않는다) 이동
- 불은 각 지점에서 네 방향으로 확산된다.
- 지훈이는 미로의 가장자리에 접한 공간에서 탈출할 수 있다.
- 지훈이와 불은 벽이 있는 공간은 통과하지 못한다.

[탈출 지점]
- 현재 이동할 수 있는 위치이며 현재 위치를 기준으로 상하좌우 방향 중 바깥 영역의 위치인 경우
"""
from sys import maxsize
from collections import deque

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

R, C = map(int, input().split())
miro = [list(input().strip()) for _ in range(R)]
f_dist = [[0] * C for _ in range(R)]
j_dist = [[0] * C for _ in range(R)]

js = deque()
fires = deque()

for i in range(R):
    for j in range(C):
        if miro[i][j] == 'J':
            j_dist[i][j] = 1
            js.append((i, j))

        if miro[i][j] == 'F':
            f_dist[i][j] = 1
            fires.append((i, j))

# 불 먼저 이동!
while fires:
    x, y = fires.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue

        if miro[nx][ny] == '#' or f_dist[nx][ny] > 0:
            continue

        f_dist[nx][ny] = f_dist[x][y] + 1
        fires.append((nx, ny))

is_exit = False
answer = -1

# 지훈이 이동
while js and not is_exit:
    x, y = js.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            answer = j_dist[x][y]
            is_exit = True
            break

        if miro[nx][ny] == '#' or j_dist[nx][ny] > 0:
            continue

        # 현재 지훈이가 가고자 하는 방향으로 가는 시간이 불이 먼저 번졌다면 패스
        if f_dist[nx][ny] and j_dist[x][y] + 1 >= f_dist[nx][ny]:
            continue

        j_dist[nx][ny] = j_dist[x][y] + 1
        js.append((nx, ny))

print('IMPOSSIBLE' if not is_exit else answer)
