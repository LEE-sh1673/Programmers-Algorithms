from copy import deepcopy
from sys import stdin

input = stdin.readline
n = 4
board = [[] for _ in range(n)]
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
# dir_x = [-1, -1, 0, 1, 1, 1, 0, -1]
# dir_y = [0, -1, -1, -1, 0, 1, 1, 1]
max_score = 0

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(0, n * 2, 2):
        board[i].append([data[j], data[j + 1] - 1])


def dfs(shark_x, shark_y, score, board):
    global max_score
    score += board[shark_x][shark_y][0]
    max_score = max(max_score, score)
    board[shark_x][shark_y][0] = 0

    # 물고기들을 이동시킨다.
    for fish in range(1, 17):
        x, y = -1, -1

        # 물고기의 위치를 구한다.
        for i in range(n):
            for j in range(n):
                if board[i][j][0] == fish:
                    x, y = i, j
                    break

        if x == -1 and y == -1:
            continue

        # 물고기가 이동할 방향을 구한다.
        direction = board[x][y][1]

        for i in range(8):
            next_direction = (direction + i) % 8
            dir_x, dir_y = directions[next_direction]
            dx = x + dir_x
            dy = y + dir_y

            if not (0 <= dx < n and 0 <= dy < n) or (dx == shark_x and dy == shark_y):
                continue

            board[x][y][1] = next_direction
            board[x][y], board[dx][dy] = board[dx][dy], board[x][y]
            break

    # 이동시킬 후보를 찾아 탐색을 진행한다.
    shark_direction = board[shark_x][shark_y][1]
    dir_x, dir_y = directions[shark_direction]

    for i in range(1, n + 1):
        dx = shark_x + dir_x * i
        dy = shark_y + dir_y * i

        if (0 <= dx < n and 0 <= dy < n) and board[dx][dy][0] > 0:
            dfs(dx, dy, score, deepcopy(board))


dfs(0, 0, 0, board)
print(max_score)
