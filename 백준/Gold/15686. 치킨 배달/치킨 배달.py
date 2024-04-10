"""
15686. 치킨 배달

- 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나
- r과 c는 1부터 시작한다.
- 각각의 집은 치킨 거리를 가지고 있다.
- <치킨 거리> = 집과 가장 가까운 치킨집 사이의 거리
- <도시 치킨 거리> = 모든 집의 치킨 거리의 합
- 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리 = |r1-r2| + |c1-c2|

도시의 치킨 집 중 임의의 m개를 고르고, 나머지 치킨집을 폐업시켰을 때 <도시 치킨 거리>의 최소값을 구하는 문제

1. 임의의 m개의 치킨집을 고른다. (13~1Cm)
2. 각 조합에 대해 다음 연산을 적용한다.
    1. 각 집의 <치킨 거리>를 구한다. (m * 2N)
        <치킨 거리> = min(집의 좌표 (r1, c1) 과 치킨집 좌표 (r2, r2)의 거리)
    2. <도시 치킨 거리>를 구한다. (m)
        <도시 치킨 거리> = sum(모든 <치킨 거리>)
"""
from itertools import combinations
from sys import maxsize

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))

"""
2. 각 조합에 대해 다음 연산을 적용한다.
    1. 각 집의 <치킨 거리>를 구한다. (m * 2N)
        <치킨 거리> = min(집의 좌표 (r1, c1) 과 치킨집 좌표 (r2, r2)의 거리)
    2. <도시 치킨 거리>를 구한다. (m)
        <도시 치킨 거리> = sum(모든 <치킨 거리>)
"""

# 임의의 m개의 치킨집을 고른다.
test = list(combinations(chickens, m))


# 각 집의 <치킨 거리>를 구한다. (m * 2N)
def dist(house, chicken):
    r1, c1 = house
    r2, c2 = chicken
    return abs(r2 - r1) + abs(c2 - c1)


answer = maxsize
for chicken_comb in test:
    city_dist = 0
    for house in houses:
        min_dist = maxsize
        for chicken in chicken_comb:
            min_dist = min(min_dist, dist(house, chicken))
        city_dist += min_dist
    answer = min(answer, city_dist)

print(answer)
