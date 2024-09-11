"""

"""
from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    INF = float('inf')
    answer = INF
    
    def dfs(i, j):
        nonlocal answer
        que = deque()
        que.appendleft((i, j, 1))
        visited = [[False for _ in range(m)] for _ in range(n)]
        visited[i][j] = True
        
        while que:
            x, y, steps = que.pop()
            
            if x == n-1 and y == m-1:
                answer = min(answer, steps)
                
            for dir_x, dir_y in [(-1,0), (1,0), (0,-1), (0,1)]:
                pos_x = x + dir_x
                pos_y = y + dir_y
            
                if pos_x < 0 or pos_x >= n or pos_y < 0 or pos_y >= m:
                    continue
                
                if maps[pos_x][pos_y] == 0 or visited[pos_x][pos_y]:
                    continue
                
                visited[pos_x][pos_y] = True
                que.appendleft((pos_x, pos_y, steps + 1))
                
    dfs(0, 0)
    return -1 if answer == INF else answer
