"""
21608. 상어 초등학교

[유형]
- 구현

[규칙]
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. <1>을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. <2>를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

[풀이]
1. N과 N^2만큼 [학생 번호, 학생이 좋아하는 학생 4명]을 입력받는다.
2. 각 학생 별로 다음을 적용한다.
    2.1 각 학생이 앉을 수 있는 자리를 탐색하다.
    2.2 자리에 인전한 좋아하는 학생 수를 구한다.
    2.3 자리에 인접한 비어있는 칸의 개수를 구한다.
    2.4 (-좋아하는 학생 수, -비어있는 칸 개수, 행 번호, 열 번호) 순으로 정렬한다.
    2.5 첫 번째 요소를 반환한다.
"""
from sys import stdin

input = stdin.readline
n = int(input())
chairs = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
followings = {}

for _ in range(n ** 2):
    student, *likes = map(int, input().split())
    followings[student] = likes


def assign_seat(student):
    candidates = []

    for i in range(n):
        for j in range(n):

            if visited[i][j]:
                continue

            like_count = 0
            blank_count = 0

            for dir_x, dir_y in directions:
                dx = i + dir_x
                dy = j + dir_y

                if dx < 0 or dx > n - 1 or dy < 0 or dy > n - 1:
                    continue

                if chairs[dx][dy] == 0:
                    blank_count += 1

                if chairs[dx][dy] in followings[student]:
                    like_count += 1

            candidates.append((like_count, blank_count, i, j))

    _, _, x, y = sorted(candidates, key=lambda c: (-c[0], -c[1], c[2], c[3]))[0]
    chairs[x][y] = student
    visited[x][y] = True


def calc_satisfaction(i, j):
    like_count = 0

    for dir_x, dir_y in directions:
        dx = i + dir_x
        dy = j + dir_y

        if dx < 0 or dx > n - 1 or dy < 0 or dy > n - 1:
            continue

        if chairs[dx][dy] in followings[chairs[i][j]]:
            like_count += 1

    return 10 ** (like_count - 1) if like_count > 0 else 0


# 자리 배정
for student in followings:
    assign_seat(student)

# 선호도 측정
print(sum([calc_satisfaction(i, j) for i in range(n) for j in range(n)]))
