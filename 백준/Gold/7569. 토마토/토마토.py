"""
7569. 토마토
"""
from sys import stdin
from collections import deque

input = stdin.readline

dirs = [
    (-1, 0, 0), (1, 0, 0),
    (0, 0, -1), (0, 0, 1),
    (0, -1, 0), (0, 1, 0)
]

def solution():
    def dfs():
        while que:
            k, i, j = que.popleft()
        
            for dir_z, dir_x, dir_y in dirs:
                z = k + dir_z
                x = i + dir_x
                y = j + dir_y 

                if z < 0 or z > h-1 or x < 0 or x > n - 1 or y < 0 or y > m - 1:
                    continue

                if tomatoes[z][x][y] == 0:
                    tomatoes[z][x][y] = tomatoes[k][i][j] + 1
                    que.append((z, x, y))

    m, n, h = map(int, input().split())
    tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    que = deque()
    
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomatoes[k][i][j] == 1:
                    que.append((k, i, j))

    answer = 0
    dfs()

    for k in range(h):
        for i in range(n):
            for j in range(m):
                if tomatoes[k][i][j] == 0:
                    return -1
                    
                answer = max(answer, tomatoes[k][i][j])

    return answer-1


print(solution())
