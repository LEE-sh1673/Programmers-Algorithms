"""
14502. 연구소

- n * m 크기의 배열
- 연구소는 빈칸, 벽으로 이루어짐
- 일부 칸은 바이러스 존재, 상하좌우로 퍼질 수 있음
- 새로 세울 수 있는 벽의 개수는 3개, (반드시 3개를 세워야 함)

[유형]
- BFS

[풀이]
1. 주어진 연구소에서 빈칸의 위치를 구한다.
    - 이때 빈칸의 개수를 저장해둔다.
2. 빈칸에서 임의로 3개를 조합하는 경우를 구한다.
3. <2>에서 얻은 경우의 수를 적용했을 때의 안전 영역의 크기를 구한다.
4. <3>에서 계산한 안전 영역의 크기 중 최대 크기를 출력한다.
"""
from collections import deque
from itertools import combinations
from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
laboratory = []
viruses = []
blanks = []
blank_count = 0

for i in range(n):
    laboratory.append([])
    for j, el in enumerate(map(int, input().split())):
        if el == 0:
            blanks.append((i, j))
            blank_count += 1

        if el == 2:
            viruses.append((i, j))

        laboratory[i].append(el)


def count_safety_area(walls):
    que = deque()
    visited = [[False] * m for _ in range(n)]
    labs = [[laboratory[i][j] for j in range(m)] for i in range(n)]
    area_count = blank_count - 3

    # 빈칸에 벽을 세움
    for i, j in walls:
        visited[i][j] = True
        labs[i][j] = 1

    # 탐색 시작 지점 할당
    for i, j in viruses:
        visited[i][j] = True
        que.append((i, j))

    while que:
        x, y = que.popleft()
        visited[x][y] = True

        for dir_x, dir_y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dx = x + dir_x
            dy = y + dir_y

            if dx < 0 or dx > n - 1 or dy < 0 or dy > m - 1:
                continue

            if labs[dx][dy] == 1:
                continue

            if not visited[dx][dy] and labs[dx][dy] == 0:
                visited[dx][dy] = True
                que.append((dx, dy))
                labs[dx][dy] = 2
                area_count -= 1

    return area_count


print(max([count_safety_area(walls) for walls in combinations(blanks, 3)]))
