"""
2667. 단지번호붙이기
"""


def bfs(i, j):
    que = [(i, j)]
    nums_house = 1
    houses[i][j] = 0
    
    while que:
        i, j = que.pop(0)
        
        for dir_x, dir_y in [(0,1),(0,-1),(1,0),(-1,0)]:
            x = i + dir_x
            y = j + dir_y
            
            if x < 0 or x > n-1 or y < 0 or y > n-1:
                continue
            
            if houses[x][y] == 1:
                houses[x][y] = 0
                que.append((x, y))
                nums_house += 1
                
    return nums_house


n = int(input())
houses = [[int(el) for el in input()] for _ in range(n)]
groups = []

for i in range(n):
    for j in range(n):
        if houses[i][j]:
            groups.append(bfs(i, j))

groups.sort()
print(len(groups))
print('\n'.join(map(str, groups)))
