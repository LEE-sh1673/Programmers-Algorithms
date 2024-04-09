"""
14889. 스타트와 링크
"""
from itertools import combinations
from sys import maxsize, stdin

input = stdin.readline
N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]
S = []

for i in combinations(range(N), N // 2):
    curr_power = 0
    for x, y in combinations(i, 2):
        curr_power += powers[x][y] + powers[y][x]
    S.append(curr_power)

s_len = len(S)
answer = maxsize

for i in range(s_len // 2):
    answer = min(answer, abs(S[s_len - i - 1] - S[i]))
print(answer)
