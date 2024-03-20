from sys import stdin
from collections import deque

input = stdin.readline


def solution():
    def dfs():
        while que:
            i, j = que.popleft()

            for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = i + dir_x
                y = j + dir_y

                if x < 0 or x > n - 1 or y < 0 or y > m - 1:
                    continue

                if tomatoes[x][y] == 0:
                    tomatoes[x][y] = tomatoes[i][j] + 1
                    que.append((x, y))

    m, n = map(int, input().split())
    tomatoes = [list(map(int, input().split())) for _ in range(n)]
    que = deque()

    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 1:
                que.append((i, j))

    answer = 0
    dfs()

    for i in range(n):
        for j in range(m):
            if tomatoes[i][j] == 0:
                return -1

            answer = max(answer, tomatoes[i][j])

    return answer-1


print(solution())
