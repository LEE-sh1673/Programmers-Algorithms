"""
20056. 마법사 상어와 파이어볼
"""
import math
from collections import defaultdict

dx8 = (-1, -1, 0, 1, 1, 1, 0, -1)
dy8 = (0, 1, 1, 1, 0, -1, -1, -1)


def split(balls):
    first_ball, *others = balls
    r1, c1, m1, s1, d1 = first_ball

    total_mass = m1
    total_speed = s1
    total_directions = [d1]
    ball_count = len(others) + 1

    for other in others:
        total_mass += other[2]
        total_speed += other[3]
        total_directions.append(other[-1])

    total_mass = math.floor(total_mass / 5)
    total_speed = math.floor(total_speed / ball_count)
    next_directions = [1, 3, 5, 7]

    if total_mass == 0:
        return []

    if all(d % 2 == 0 for d in total_directions) \
            or all(d % 2 != 0 for d in total_directions):
        next_directions = [0, 2, 4, 6]

    return [[r1, c1, total_mass, total_speed, d] for d in next_directions]


def move(ball):
    r, c, m, s, d = ball
    next_r = (r + dx8[d] * s) % n
    next_c = (c + dy8[d] * s) % n
    return [next_r, next_c, m, s, d]


n, m, k = map(int, input().split())
fire_balls = [list(map(int, input().split())) for _ in range(m)]

for _ in range(k):
    moved_balls = []
    positions = defaultdict(list)

    while fire_balls:
        moved_ball = move(fire_balls.pop())
        moved_balls.append(moved_ball)
        r, c, _, _, _ = moved_ball
        positions[n * r + c].append(moved_ball)

    for ball in moved_balls:
        r, c, _, _, _ = ball
        if len(positions[n * r + c]) == 1:
            fire_balls.append(ball)

    for idx, balls in positions.items():
        if len(balls) >= 2:
            split_balls = split(balls)
            fire_balls += split_balls

print(sum([ball[2] for ball in fire_balls]))
