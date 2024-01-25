"""
- 각 칸은 통로 또는 벽으로 구성
- 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동 가능
- 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동
    - 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있음
- 미로에서 한 칸을 이동하는데 1초가 걸림
- 미로를 탈출하는데 필요한 최소 시간을 return, 탈출할 수 없다면 -1
"""
def solution(maps):

    def bfs(start, end):
        x, y = start
        dest_x, dest_y = end
        
        map_rows = len(maps)
        map_cols = len(maps[0])
        visited = [[False for _ in range(map_cols)] for _ in range(map_rows)]
        
        que = [(x, y, 0)]
        visited[x][y] = True

        while que:
            x, y, cnt = que.pop(0)

            for dir_x, dir_y in [(1,0), (-1,0), (0,1), (0,-1)]:
                pos_x = x + dir_x
                pos_y = y + dir_y

                if pos_x < 0 or pos_x > map_rows-1 or pos_y < 0 or pos_y > map_cols-1:
                    continue

                if maps[pos_x][pos_y] == "X":
                    continue

                if maps[pos_x][pos_y] == maps[dest_x][dest_y]:
                    return cnt + 1

                if not visited[pos_x][pos_y]:
                    visited[pos_x][pos_y] = True
                    que.append((pos_x, pos_y, cnt+1))
        return -1
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                start = (i, j)
            if maps[i][j] == "L":
                rever = (i, j)
            if maps[i][j] == "E":
                end = (i, j)
    
    d1, d2 = bfs(start, rever), bfs(rever, end)
    
    if d1 == -1 or d2 == -1:
        return -1
    
    return d1 + d2
        