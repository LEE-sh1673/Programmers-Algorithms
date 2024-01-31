from collections import deque

INF = float('inf')


def solution(board):
    n, m = len(board), len(board[0])
    answer = INF

    def bfs(i, j):
        nonlocal answer
        que = deque()
        que.appendleft((i, j, 0))

        visited = set()
        visited.add((i, j))

        while que:
            pos_x, pos_y, step = que.pop()

            if answer <= step:
                continue

            if board[pos_x][pos_y] == 'G':
                answer = min(answer, step)
                continue

            visited.add((pos_x, pos_y))

            for dir_x, dir_y in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                dx, dy = pos_x, pos_y

                while (0 <= dx < n) and (0 <= dy < m) and board[dx][dy] != 'D':
                    dx, dy = dx + dir_x, dy + dir_y

                dx -= dir_x
                dy -= dir_y

                if (dx, dy) in visited:
                    continue

                que.appendleft((dx, dy, step + 1))

    start_x, start_y = -1, -1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start_x, start_y = i, j
                break

        if start_x != -1:
            break

    bfs(start_x, start_y)
    return -1 if answer == INF else answer
