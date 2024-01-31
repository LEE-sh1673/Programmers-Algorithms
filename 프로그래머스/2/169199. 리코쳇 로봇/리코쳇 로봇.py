from collections import deque

INF = float('inf')


def solution(board):
    n, m = len(board), len(board[0])
    answer = INF

    def bfs(i, j):
        nonlocal answer
        visited = [[False for _ in range(m)] for _ in range(n)]
        que = deque()
        que.appendleft((i, j, 0))

        while que:
            pos_x, pos_y, step = que.pop()

            if answer <= step:
                continue

            if board[pos_x][pos_y] == 'G':
                answer = min(answer, step)
                continue

            for dir_x, dir_y in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                dx, dy = pos_x, pos_y

                while (0 <= dx < n) and (0 <= dy < m) and board[dx][dy] != 'D':
                    dx += dir_x
                    dy += dir_y

                dx -= dir_x
                dy -= dir_y

                if visited[dx][dy]:
                    continue

                visited[dx][dy] = True
                que.appendleft((dx, dy, step + 1))
                # print(que)

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


# print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
