"""
16236. 아기 상어

- 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없다.
- 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다.
- 아기 상어는 자신의 크기와 같은 물고기를 먹을 수는 없지만, 칸을 지날 수 있다.

[행동 방식]
1. 더 이상 먹을 수 있는 물고기가 없다면 엄마 상어에게 도움을 요청
2. 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
3. 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
4.
    4-1. 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기를 먹음
    4-2. 그러한 물고기가 여러 마리라면, 가장 왼쪽에 있는 물고기를 먹음


(거리) = 아기 상어 칸 ~ 물고기 칸 이동 시, 지나야하는 칸의 개수의 최솟값
아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다.

아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
"""
from collections import deque
from sys import stdin

input = stdin.readline


class Fish:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist


class Shark:
    def __init__(self, x=0, y=0, size=2):
        self.x = x
        self.y = y
        self.size = size
        self.distance = 0
        self.eat_count = 0

    def eat(self, fish):
        self.move_to(fish.x, fish.y)
        self.add_dist(fish.dist)
        self.increase_eat_count()

    def add_dist(self, distance):
        self.distance += distance

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def increase_eat_count(self):
        self.eat_count += 1

        if self.eat_count == self.size:
            self.eat_count = 0
            self.size += 1


def bfs(i, j):
    fishes = []
    queue = deque()
    visited = [[False] * n for _ in range(n)]

    queue.append((i, j, 0))
    visited[i][j] = True

    while queue:
        i, j, cnt = queue.popleft()

        for dir_x, dir_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = i + dir_x
            y = j + dir_y

            if x < 0 or x > n - 1 or y < 0 or y > n - 1:
                continue

            if not visited[x][y] and space[x][y] <= shark.size:
                visited[x][y] = True
                queue.append((x, y, cnt + 1))

                if 0 < space[x][y] < shark.size:
                    fishes.append(Fish(x, y, cnt + 1))

    return sorted(fishes, key=lambda fish: (fish.dist, fish.x, fish.y))


n = int(input())
space = [list(map(int, input().strip().split())) for _ in range(n)]
shark = Shark()

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            shark.x = i
            shark.y = j
            break

while True:
    candidate_fishes = bfs(shark.x, shark.y)

    if not candidate_fishes:
        break

    fish = candidate_fishes[0]
    space[shark.x][shark.y] = 0
    space[fish.x][fish.y] = 0
    shark.eat(fish)

print(shark.distance)
