"""
21918. 전구
"""
from sys import stdin

n, m = map(int, stdin.readline().split())
bulbs = list(map(int, stdin.readline().split()))
commands = [tuple(map(int, stdin.readline().split())) for _ in range(m)]

for no, l, r in commands:
    # i 번째 전구의 상태를 x로 변경한다.
    if no == 1:
        bulbs[l-1] = r

    # l번째부터 r번째까지의 전구 상태를 변경한다.
    elif no == 2:
        for i in range(l-1, r):
            bulbs[i] = (bulbs[i] + 1) % 2

    # l번째부터 r번째까지의 전구를 끈다.
    elif no == 3:
        for i in range(l - 1, r):
            bulbs[i] = 0

    # l번째부터 r번째까지의 전구를 킨다.
    else:
        for i in range(l - 1, r):
            bulbs[i] = 1

print(*bulbs)
