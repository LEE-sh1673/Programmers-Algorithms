from collections import deque

T = int(input())

maxsize = 1e10
dx = (0, -1, 1, 0)
dy = (1, 0, 0, -1)

for test_case in range(1, T+1):
    N = int(input())
    board = [[int(num) for num in input()] for _ in range(N)]
    time = [[maxsize] * N for _ in range(N)]

    que = deque()
    que.append((0, 0))
    time[0][0] = 0

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            curr_time = time[x][y] + board[nx][ny]

            if curr_time < time[nx][ny]:
                time[nx][ny] = curr_time
                que.append((nx, ny))

    print(f'#{test_case} {time[N-1][N-1]}')
