from sys import stdin, maxsize
from itertools import combinations
from collections import deque

input = stdin.readline


def solution(n, m):
    def bfs(virus_comb, blank_count):
        que = deque()
        visited = [[False] * n for _ in range(n)]
        infect_time = 0
        
        for x, y in virus_comb:
            que.append((x, y, 0))
            visited[x][y] = True
    
        while que:
            x, y, cnt = que.popleft()
    
            for dir_x, dir_y in [(1,0),(-1,0),(0,1),(0,-1)]:
                dx = x + dir_x
                dy = y + dir_y
    
                if dx < 0 or dx > n-1 or dy < 0 or dy > n-1:
                    continue
    
                if maps[dx][dy] == 1:
                    continue
                    
                if not visited[dx][dy]:
                    visited[dx][dy] = True
                    que.append((dx, dy, cnt+1))

                    if maps[dx][dy] == 0:
                        blank_count -= 1
                        infect_time = max(infect_time, cnt+1)
        
        return infect_time if blank_count == 0 else maxsize

    
    maps = [list(map(int, input().split())) for _ in range(n)]
    viruses = []
    blank_count = 0
    
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 2:
                viruses.append((i, j))
                
            if maps[i][j] == 0:
                blank_count += 1
    
    viruses = list(combinations(viruses, m))
    min_infect_time = maxsize

    for virus in viruses:
        min_infect_time = min(min_infect_time, bfs(virus, blank_count))

    return -1 if min_infect_time == maxsize else min_infect_time


n, m = map(int, input().split())
print(solution(n, m))
