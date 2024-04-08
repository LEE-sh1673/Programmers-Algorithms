"""
19237. 청소년 상어

[물고기]
- 번호가 작은 물고기부터 순서대로 이동한다.
    - 물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸이다.
    - 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다.
- 물고기는 '방향'을 가지고 이동한다.
- 물고기는 8가지 방향(상하좌우, 대각선)을 가질 수 있다.
- 물고기는 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
    - 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다.
    - 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.


[상어]
- 물고기의 이동이 모두 끝나면 상어가 이동한다.
- 상어는 '방향'에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다.
- 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.
- 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다.
- 물고기가 없는 칸으로는 이동할 수 없다.
- 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다.
- 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.
"""
import copy
from sys import stdin

input = stdin.readline
n = 4
board = [[] for _ in range(n)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(n):
    data = list(map(int, input().split()))
    fish = []
    for j in range(0, n*2, 2):
        fish.append([data[j], data[j + 1] - 1])
    board[i] = fish

max_score = 0


def dfs(sx, sy, score, board):
    global max_score
    score += board[sx][sy][0]
    max_score = max(max_score, score)
    board[sx][sy][0] = 0

    # 물고기 움직임
    # 물고기 1번부터 16번까지 찾기
    for f in range(1, 17):
        f_x, f_y = -1, -1
        # board 뒤져서 찾기
        for x in range(n):
            for y in range(n):
                if board[x][y][0] == f:
                    f_x, f_y = x, y
                    break

        # 물고기 없으면 다음 물고기 찾기
        if f_x == -1 and f_y == -1:
            continue

        # 방향: 지금 물고기 방향
        f_d = board[f_x][f_y][1]

        # 방향에 맞춰서 물고기 자리 바꾸기, 바꿀 자리 없으면 다음 방향으로
        for i in range(8):
            nd = (f_d + i) % 8  # 처음엔 자기 방향으로 나옴
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]

            # 물고기 이동할 수 있는 자리인지 체크
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue

            board[f_x][f_y][1] = nd  # 이동 가능한 방향을 찾은걸로 갱신

            # 자리 바꿈
            board[f_x][f_y], board[nx][ny] = board[nx][ny], board[f_x][f_y]
            break

    # 상어 먹음
    s_d = board[sx][sy][1]  # 상어 방향

    # 최대 4번까지 현재 방향의 자리 탐색 가능 (1,2,3,4)
    for i in range(1, 5):
        nx = sx + dx[s_d] * i
        ny = sy + dy[s_d] * i

        # 이동 가능한 자리인지 체크한 뒤 dfs
        if (0 <= nx < 4 and 0 <= ny < 4) and board[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(board))


dfs(0, 0, 0, board)
print(max_score)
