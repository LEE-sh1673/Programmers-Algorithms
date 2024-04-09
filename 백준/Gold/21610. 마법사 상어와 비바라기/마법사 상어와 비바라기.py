from sys import stdin

input = stdin.readline
n, m = map(int, input().split())
baskets = [list(map(int, input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split())) for _ in range(m)]

dx8 = ("E", 0, -1, -1, -1, 0, 1, 1, 1)
dy8 = ("E", -1, -1, 0, 1, 1, 1, 0, -1)
dx4 = (-1, -1, 1, 1)
dy4 = (-1, 1, -1, 1)

clouds = [
    [n - 1, 0], [n - 1, 1],
    [n - 2, 0], [n - 2, 1]
]

for direction, steps in moves:
    moved_clouds = set()

    while clouds:
        x, y = clouds.pop()
        dx = (x + steps * dx8[direction]) % n
        dy = (y + steps * dy8[direction]) % n
        baskets[dx][dy] += 1
        moved_clouds.add((dx, dy))

    # 각 구름의 좌표를 (행, 열) 오름차 순 기준으로 순서대로 좌우 대각선을 비교하여 1 이상인 값의 횟수를 구한다. (N)
    for x, y in moved_clouds:
        water_count = 0
        for i in range(4):
            dx = x + dx4[i]
            dy = y + dy4[i]

            if dx < 0 or dx > n - 1 or dy < 0 or dy > n - 1:
                continue

            if baskets[dx][dy] > 0:
                water_count += 1

        baskets[x][y] += water_count

    # cloud 좌표에 해당하는 값을 제외한 필드를 순회하여 값이 2 이상인 값을 새로 클라우드에 담는다. (N^2)
    for i in range(n):
        for j in range(n):
            if (i, j) in moved_clouds or baskets[i][j] < 2:
                continue
            baskets[i][j] -= 2
            clouds.append((i, j))

print(sum([sum(_) for _ in baskets]))
