from sys import stdin

input = stdin.readline


def solution():
    def dfs(i, j):
        que = [(i, j)]
        
        while que:
            i, j = que.pop(0)
        
            for dir_x, dir_y in [(-1,0),(0,1),(1,0),(0,-1)]:
                x = i + dir_x
                y = j + dir_y
            
                if x < 0 or x > n-1 or y < 0 or y > m-1:
                    continue
            
                if fields[x][y] == 1:
                    que.append((x, y))
                    fields[x][y] = 0
            

    for _ in range(int(input())):
        n, m, k = map(int, input().split())
        fields = [[0] * m for _ in range(n)]
        answer = 0

        for _ in range(k):
            i, j = map(int, input().split())
            fields[i][j] = 1
    
        for i in range(n):
            for j in range(m):
                if fields[i][j]:
                    answer += 1
                    dfs(i, j)
    
        print(answer)
    
solution()
